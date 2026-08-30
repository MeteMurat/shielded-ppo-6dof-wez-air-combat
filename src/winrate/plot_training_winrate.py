# plot_training_winrate.py
import numpy as np
import matplotlib.pyplot as plt
import math
from pathlib import Path

def load_agent_logs(agent_name, dir_path, n_logs=10):
    """
    dir_path: win_loss_tight*.npy dosyalarının olduğu klasör.
    Her bir win_loss_tight{i}.npy dosyasının SON satırından (kümülatif) wins/losses/ties alır,
    hepsini toplayarak toplam istatistiği döndürür.
    """
    dir_path = Path(dir_path)
    total_wins = 0
    total_losses = 0
    total_ties = 0

    for i in range(n_logs):
        fpath = dir_path / f"win_loss_tight{i}.npy"
        if not fpath.exists():
            print(f"[WARN] {agent_name}: {fpath} bulunamadı, atlanıyor.")
            continue
        arr = np.load(fpath)
        if arr.ndim != 2 or arr.shape[1] < 3:
            raise ValueError(f"{fpath} beklenen formatta değil (shape={arr.shape}).")
        wins, losses, ties = arr[-1]  # son satır: kümülatif
        total_wins   += int(wins)
        total_losses += int(losses)
        total_ties   += int(ties)

    total_episodes = total_wins + total_losses + total_ties
    if total_episodes == 0:
        raise ValueError(f"{agent_name}: toplam bölüm sayısı 0 görünüyor, loglar boş olabilir.")

    # Saf win-rate (ties hariç)
    p_win = total_wins / total_episodes
    # “win + 0.5·tie” efektif başarı oranı
    p_eff = (total_wins + 0.5 * total_ties) / total_episodes

    return {
        "wins": total_wins,
        "losses": total_losses,
        "ties": total_ties,
        "total": total_episodes,
        "p_win": p_win,
        "p_eff": p_eff,
    }

def wilson_ci(p_hat, n, z=1.96):
    """
    Binom için 95% Wilson güven aralığı.
    Burada p_hat'i yaklaşık başarı olasılığı (örn. p_eff) olarak kullanıyoruz.
    """
    if n == 0:
        return 0.0, 0.0
    denom = 1.0 + z**2 / n
    center = (p_hat + z**2 / (2*n)) / denom
    margin = z * math.sqrt((p_hat*(1-p_hat)/n) + (z**2/(4*n**2))) / denom
    lo = max(0.0, center - margin)
    hi = min(1.0, center + margin)
    return lo, hi

def main():
    # Bu script'i şu klasöre koyduğunu varsayıyorum:
    # C:\Users\PC\Desktop\dogfight-kod-chatatılacak\winrate
    base_dir = Path(__file__).resolve().parent

    # Senin verdiğin klasör isimlerine göre:
    paths = {
        "DDQN":   base_dir / "RL-win-loss",
        "Hybrid": base_dir / "win-loss-hybrid",
        "PPO":    base_dir / "ppo-win-loss",
    }

    labels = []
    means = []
    lower_err = []
    upper_err = []

    print("=== Training-log based effective win rates (win + 0.5·tie) ===")
    for agent_name, dir_path in paths.items():
        stats = load_agent_logs(agent_name, dir_path, n_logs=10)
        total = stats["total"]
        p_eff = stats["p_eff"]

        # %95 Wilson CI (p_eff üzerinden yaklaşık olarak)
        ci_lo, ci_hi = wilson_ci(p_eff, total)
        labels.append(agent_name)
        means.append(p_eff)
        lower_err.append(p_eff - ci_lo)
        upper_err.append(ci_hi - p_eff)

        print(
            f"{agent_name}: wins={stats['wins']}, "
            f"losses={stats['losses']}, ties={stats['ties']}, "
            f"total={total}, p_eff={p_eff:.3f}, "
            f"95% CI=[{ci_lo:.3f}, {ci_hi:.3f}]"
        )

    x = np.arange(len(labels))

    plt.figure(figsize=(6, 4))
    plt.bar(x, means, yerr=[lower_err, upper_err], capsize=5)
    plt.xticks(x, labels)
    plt.ylabel("Effective win rate (win + 0.5·tie)")
    plt.ylim(0.0, 1.0)
    plt.title("Training-log based effective win rates with 95% CI")
    plt.tight_layout()

    out_name = base_dir / "training_winrate_comparison.pdf"
    plt.savefig(out_name, dpi=300)
    print(f"\nBar grafiği kaydedildi: {out_name}")
    plt.show()

if __name__ == "__main__":
    main()
