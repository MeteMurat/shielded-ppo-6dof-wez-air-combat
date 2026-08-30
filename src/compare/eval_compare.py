import os
import sys
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# --- Env paketini path'e ekle ---
BASE_DIR = os.path.dirname(__file__)  # eval_compare.py'nin olduğu klasör (compare)

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from Env import Env  # type: ignore[import]
except ModuleNotFoundError as exc:
    raise ImportError(
        "Env paketine ulaşılamıyor. 'compare' klasörünün yanında 'Env' paketinin"
        " olduğundan ve __init__.py içerdiğinden emin olun."
    ) from exc


# --- Ortak Q ağı (üç model de aynı mimariyi kullanıyor) ---
class QNet(nn.Module):
    def __init__(self, state_dim=13, n_actions=8):
        super().__init__()
        self.feature = nn.Sequential(
            nn.Linear(state_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, n_actions),
        )

    def forward(self, x):
        return self.feature(x)


def load_qnet(pth_path, state_dim=13, n_actions=8, device="cpu"):
    net = QNet(state_dim=state_dim, n_actions=n_actions).to(device)
    state_dict = torch.load(pth_path, map_location=device)
    net.load_state_dict(state_dict)
    net.eval()
    return net


# --- 95% bootstrap CI hesaplayıcı ---
def bootstrap_ci_95(x, n_boot=10000, random_state=0):
    x = np.asarray(x, dtype=float)
    rng = np.random.default_rng(random_state)
    means = []
    for _ in range(n_boot):
        sample = rng.choice(x, size=len(x), replace=True)
        means.append(sample.mean())
    lower = np.percentile(means, 2.5)
    upper = np.percentile(means, 97.5)
    return lower, upper


# --- Tek ajan evaluation ---
def evaluate_agent(net, n_episodes=100, max_steps=300, device="cpu"):
    """
    Her bölümün sonucunu:
      1.0 = Red win
      0.5 = tight (ikisi birden ölürse)
      0.0 = loss
    olarak döndürür.
    """
    env = Env()
    results = []

    for ep in range(n_episodes):
        reset_out = env.reset()
        # Bazı Env.reset() fonksiyonları (obs, info) döner; sadece obs'i alalım
        if isinstance(reset_out, tuple):
            state = reset_out[0]
        else:
            state = reset_out

        if state is None:
            print(f"[WARN] Episode {ep+1}: env.reset() None döndü, atlanıyor.")
            continue

        done = False
        step = 0
        last_reward = 0.0

        while not done and step < max_steps:
            state_arr = np.asarray(state, dtype=np.float32).reshape(1, -1)
            state_tensor = torch.from_numpy(state_arr).to(device)

            with torch.no_grad():
                q_values = net(state_tensor)
                action = int(torch.argmax(q_values, dim=1).item())

            step_out = env.step(action)

            # step çıktısı 3 veya 4 elemanlı olabilir
            if isinstance(step_out, tuple):
                if len(step_out) == 3:
                    next_state, reward, done = step_out
                else:
                    next_state, reward, done, info = step_out
            else:
                # Çok sıra dışı bir durum; üçlüye zorla aç
                next_state, reward, done = step_out

            last_reward = reward
            state = next_state
            step += 1

        # Bölüm sonunda sonucu sınıflandır
        # Tercihen env.red_blood / env.blue_blood kullanılacak:
        red_blood = getattr(env, "red_blood", None)
        blue_blood = getattr(env, "blue_blood", None)

        if (red_blood is not None) and (blue_blood is not None):
            if red_blood <= 0:
                if blue_blood <= 0:
                    outcome = 0.5  # tight
                else:
                    outcome = 1.0  # Red win
            else:
                outcome = 0.0      # Red kaybetmiş
        else:
            # Fallback: sadece son reward'a bak (gerekirse değiştir)
            if last_reward > 0:
                outcome = 1.0
            elif last_reward < 0:
                outcome = 0.0
            else:
                outcome = 0.5

        results.append(outcome)

    return np.array(results, dtype=float)


def main():
    device = "cpu"  # GPU kullanmak istersen "cuda" yapabilirsin

    # --- .pth dosyalarının isimleri (compare klasöründe) ---
    # Bu dosyalar C:\Users\PC\Desktop\dogfight-kod-chatatılacak\compare içinde olmalı
    models = [
        ("DDQN",   "rl_49_Q_Net.pth"),
        ("Hybrid", "hibrid_50_Q_Net.pth"),
        ("PPO",    "ppo_30_Q_Net.pth"),
    ]

    # Kaç bölümle değerlendireceksin? Makale ile uyumlu olsun (örneğin 100).
    N_EVAL = 100
    MAX_STEPS = 300

    all_means = []
    all_lower = []
    all_upper = []
    all_raw = {}

    for name, fname in models:
        if not os.path.exists(fname):
            raise FileNotFoundError(f"{fname} bu klasörde bulunamadı!")

        print(f"\n=== Evaluating {name} ({fname}) ===")
        net = load_qnet(fname, state_dim=13, n_actions=8, device=device)
        results = evaluate_agent(net, n_episodes=N_EVAL, max_steps=MAX_STEPS, device=device)

        # Win-rate tanımı: win + 0.5 * tight
        mean_wr = results.mean()
        lo, hi = bootstrap_ci_95(results, n_boot=10000, random_state=0)

        print(f"{name} mean win-rate (win + 0.5·tight): {mean_wr:.3f}")
        print(f"{name} 95% CI: [{lo:.3f}, {hi:.3f}]")

        all_means.append(mean_wr)
        all_lower.append(mean_wr - lo)
        all_upper.append(hi - mean_wr)
        all_raw[name] = results

        # Ham sonuçları da sakla (reprodüksiyon için)
        np.save(f"{name.lower()}_eval_results.npy", results)

    # --- Bar grafiği çiz ---
    agents = [m[0] for m in models]
    x = np.arange(len(agents))

    plt.figure(figsize=(6, 4))
    plt.bar(x, all_means, yerr=[all_lower, all_upper], capsize=5)
    plt.xticks(x, agents)
    plt.ylabel("Win rate (win + 0.5·tight)")
    plt.ylim(0.0, 1.0)
    plt.title(f"Post-training win rates over {N_EVAL} evaluation episodes")
    plt.tight_layout()

    out_name = "winrate_comparison.pdf"
    plt.savefig(out_name, dpi=300)
    print(f"\nBar grafiği kaydedildi: {out_name}")
    plt.show()


if __name__ == "__main__":
    # Bazı ortamlar için gerekebilir:
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    main()
