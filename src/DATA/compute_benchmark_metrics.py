# compute_benchmark_metrics.py
import os, re, math, json, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------
# IO helper: tek episode .npz okuyucu
# ------------------------
def load_episode_npz(path):
    z = np.load(path, allow_pickle=True)

    def pick(*names, default=None):
        for n in names:
            if n in z:
                return z[n]
        return default

    ata = pick('ata', 'ATA', 'ATA_deg', 'antenna_angle')
    dist = pick('dist', 'distance', 'd')
    alt  = pick('alt', 'altitude', 'h', 'height')
    gy   = pick('g_force_y', 'gy')
    gz   = pick('g_force_z', 'gz')
    gtot = pick('g_total')
    if gtot is None and gy is not None and gz is not None:
        gtot = np.sqrt(gy**2 + gz**2)

    mach      = pick('mach', 'Mach')
    wez_flag  = pick('wez_flag')
    done_cause = pick('done_cause')

    # ---- meta: agent / seed / episode ----
    fname  = os.path.basename(path)
    parent = os.path.basename(os.path.dirname(path))
    tag_source = fname + "_" + parent  # hem isim hem klasör

    # agent adı
    m = re.search(r'(ppo|ddqn|hybrid|hibrid|rl)', tag_source, re.I)
    if m:
        tag = m.group(1).lower()
        if tag == 'ppo':
            agent = 'PPO'
        elif tag in ('hybrid', 'hibrid'):
            agent = 'HYBRID'
        elif tag in ('ddqn', 'rl'):
            agent = 'DDQN'  # RL klasörünü DDQN tabanlı RL ajanı olarak kabul ediyoruz
        else:
            agent = tag.upper()
    else:
        agent = 'AGENT'

    # seed
    m = re.search(r'seed[_\-]?(\d+)', tag_source, re.I)
    seed = int(m.group(1)) if m else -1

    # episode no
    m = re.search(r'episode[_\-]?(\d+)', tag_source, re.I)
    epi = int(m.group(1)) if m else -1

    return dict(path=path, agent=agent, seed=seed, episode=epi,
                ata=ata, dist=dist, alt=alt, mach=mach,
                gtot=gtot, wez_flag=wez_flag, done_cause=done_cause)

# ------------------------
# Metrik hesaplayıcı yardımcılar
# ------------------------
def bool_wez(dist, ata, theta_deg=3.0, dmin=100.0, dmax=1000.0):
    if dist is None or ata is None:
        return None
    # ata rad ise dereceye çevir
    ata_deg = ata
    if np.nanmax(np.abs(ata)) < 0.5:
        ata_deg = np.degrees(ata)
    return (dist >= dmin) & (dist <= dmax) & (np.abs(ata_deg) < theta_deg)

def first_pass_time_to_merge(dist, d_star=500.0, dt=1.0):
    if dist is None:
        return np.nan
    idx = np.where(dist <= d_star)[0]
    return (idx[0] * dt) if len(idx) > 0 else np.nan

# ------------------------
# Tüm klasörü özetle
# ------------------------
def summarize_folder(folder, theta_list=(1.0, 3.0, 5.0),
                     dwin=(100.0, 1000.0), h_star=150.0):
    """
    h_star: metre cinsinden güvenlik irtifası (~150 m ≈ 500 ft)
    """
    rows = []
    files = glob.glob(os.path.join(folder, '**', '*.npz'), recursive=True)
    if not files:
        print("No .npz files found under", folder)
    for f in files:
        ep = load_episode_npz(f)
        ata  = ep['ata']
        dist = ep['dist']
        alt  = ep['alt']
        gtot = ep['gtot']

        if ata is None or dist is None:
            continue

        dt = 1.0  # 1 RL adımı = 1 s (100*0.01)

        # Altitude deficit (episode-level mean, normalize to [0,1])
        if alt is not None:
            Th = np.maximum(0.0, h_star - alt) / h_star
            H_deficit_mean = float(np.nanmean(Th))
        else:
            H_deficit_mean = math.nan

        # ata'yı dereceye çevir
        ata_deg = ata
        if np.nanmax(np.abs(ata)) < 0.5:
            ata_deg = np.degrees(ata)

        for theta in theta_list:
            wez = ep['wez_flag']
            if wez is None:
                wez = bool_wez(dist, ata, theta_deg=theta,
                               dmin=dwin[0], dmax=dwin[1])

            wez_occ = math.nan if wez is None else 100.0 * np.mean(wez.astype(float))

            # Sustained ATA: |ATA| ortalaması, |ATA| < theta bandı içinde
            sust_ata = math.nan
            mask = np.abs(ata_deg) < theta
            if np.any(mask):
                sust_ata = float(np.nanmean(np.abs(ata_deg[mask])))

            ttm = first_pass_time_to_merge(dist,
                                           d_star=0.5 * (dwin[0] + dwin[1]),
                                           dt=dt)
            g_int = float(np.trapz(gtot, dx=dt)) if gtot is not None else math.nan

            rows.append(dict(agent=ep['agent'],
                             seed=ep['seed'],
                             episode=ep['episode'],
                             theta=theta,
                             WEZ_occ_pct=wez_occ,
                             Sustained_ATA_deg=sust_ata,
                             TimeToMerge_s=ttm,
                             G_exposure=g_int,
                             H_deficit_mean=H_deficit_mean,
                             done_cause=ep['done_cause']))
    return pd.DataFrame(rows)

# ------------------------
# İstatistik yardımcıları ve çıktı
# ------------------------
def ci95(x):
    x = np.array([v for v in x if not math.isnan(v)])
    if len(x) == 0:
        return (np.nan, np.nan)
    m = np.mean(x)
    s = np.std(x, ddof=1) / math.sqrt(len(x))
    return (m - 1.96 * s, m + 1.96 * s)

def save_raw_df(df, outdir):
    df.to_csv(os.path.join(outdir, 'episodes_raw_metrics.csv'), index=False)

def make_tables_and_plots(df, outdir):
    os.makedirs(outdir, exist_ok=True)

    # Özet tablo (agent x theta)
    summ = (df.groupby(['agent', 'theta'])
              .agg(WEZ_mean=('WEZ_occ_pct', 'mean'),
                   WEZ_lo=('WEZ_occ_pct', lambda v: ci95(v)[0]),
                   WEZ_hi=('WEZ_occ_pct', lambda v: ci95(v)[1]),
                   SustATA_mean=('Sustained_ATA_deg', 'mean'),
                   TTM_mean=('TimeToMerge_s', 'mean'),
                   Gexp_mean=('G_exposure', 'mean'))
              .reset_index())
    summ.to_csv(os.path.join(outdir, 'metrics_summary.csv'), index=False)

    # 3 panel: WEZ, Sustained-ATA, TTM
    plt.figure(figsize=(10, 8))
    ax1 = plt.subplot(3, 1, 1)
    for a, sub in summ.groupby('agent'):
        ax1.plot(sub['theta'], sub['WEZ_mean'], label=a, marker='o')
        ax1.fill_between(sub['theta'], sub['WEZ_lo'], sub['WEZ_hi'], alpha=0.2)
    ax1.set_ylabel('WEZ occupancy (%)')
    ax1.grid(True)

    ax2 = plt.subplot(3, 1, 2)
    for a, sub in summ.groupby('agent'):
        ax2.plot(sub['theta'], sub['SustATA_mean'], label=a, marker='o')
    ax2.set_ylabel('Sustained-ATA (deg)')
    ax2.grid(True)

    ax3 = plt.subplot(3, 1, 3)
    for a, sub in summ.groupby('agent'):
        ax3.plot(sub['theta'], sub['TTM_mean'], label=a, marker='o')
    ax3.set_xlabel('ATA threshold θ (deg)')
    ax3.set_ylabel('Time-to-merge (s)')
    ax3.grid(True)
    ax1.legend(ncol=3, fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, 'fig_wez_sustata_ttm.pdf'))

    # G-exposure mean±std (agent bazında, tüm theta’lar birleştirilmiş)
    plt.figure(figsize=(6, 4))
    g = df.groupby('agent')['G_exposure']
    agents = list(g.groups.keys())
    means = [g.get_group(a).mean() for a in agents]
    stds  = [g.get_group(a).std(ddof=1) for a in agents]
    xs = np.arange(len(agents))
    plt.bar(xs, means, yerr=stds, capsize=4)
    plt.xticks(xs, agents)
    plt.ylabel('G-exposure (∫||G|| dt)')
    plt.title('G-exposure (mean ±1σ)')
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, 'fig_g_exposure_mean_std.pdf'))

# ------------------------
# main
# ------------------------
if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--folder', required=True,
                    help='Root folder containing episode .npz logs (DATA; subfolders ppo/hibrid/rl)')
    ap.add_argument('--out', default='benchmark_out', help='Output folder')
    ap.add_argument('--theta', default='1,3,5', help='Comma-separated ATA thresholds in deg')
    ap.add_argument('--dwin', default='100,1000', help='Distance window min,max (m)')
    args = ap.parse_args()

    thetas = [float(x) for x in args.theta.split(',')]
    dmin, dmax = [float(x) for x in args.dwin.split(',')]

    df = summarize_folder(args.folder, theta_list=thetas, dwin=(dmin, dmax))
    if df.empty:
        raise SystemExit("No valid .npz episodes found or keys missing.")

    os.makedirs(args.out, exist_ok=True)
    save_raw_df(df, args.out)

    # Kalibrasyon sayıları: G_budget ve ortalama H_deficit
    df_epi = df.drop_duplicates(subset=['agent', 'seed', 'episode'])
    valid_g = df_epi['G_exposure'].dropna().values
    if len(valid_g) > 0:
        G_budget = float(np.quantile(valid_g, 0.95))
    else:
        G_budget = math.nan

    valid_h = df_epi['H_deficit_mean'].dropna().values
    mu_h = float(np.mean(valid_h)) if len(valid_h) > 0 else math.nan

    calib = dict(G_budget=G_budget,
                 mean_H_deficit=mu_h,
                 note="G_budget = 95th percentile of episode-level G_exposure over all agents")
    with open(os.path.join(args.out, 'calibration_stats.json'), 'w') as f:
        json.dump(calib, f, indent=2)

    print("G_budget (95th percentile G_exposure):", G_budget)
    print("Mean H_deficit (baseline):", mu_h)

    make_tables_and_plots(df, args.out)
    print(f"Done. Wrote CSV/figures to: {args.out}")
