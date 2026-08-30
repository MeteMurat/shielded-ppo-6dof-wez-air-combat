import os
import numpy as np
import matplotlib.pyplot as plt

# G-force .npz dosyalarının bulunduğu klasör
folder = r"C:\Users\90531\Desktop\g-force-HTBRİD - SABİT\hibrit-yöntem (rule based+heuretic optimization)\Dogfight-main\train\GForceTestResults"

# Tüm bileşke G-kuvvetlerini sakla
all_total = []

# Dosyaları sırayla oku
for filename in sorted(os.listdir(folder)):
    if filename.endswith(".npz") and filename.startswith("episode_"):
        path = os.path.join(folder, filename)
        data = np.load(path)

        # Gz ve Gy bileşenleri
        g_z = data["g_force_z"]
        g_y = data["g_force_y"]

        # Bileşke G-force
        g_total = np.sqrt(g_z**2 + g_y**2)
        all_total.append(g_total)

# En kısa epizod uzunluğuna göre kırp
min_len = min(len(g) for g in all_total)
all_trimmed = np.array([g[:min_len] for g in all_total])

# Ortalama ve standart sapma
mean_total = np.mean(all_trimmed, axis=0)
std_total = np.std(all_trimmed, axis=0)
steps = np.arange(min_len)

# Grafik: sadece bileşke G-force + hata bölgesi
plt.figure(figsize=(10, 6))
plt.plot(steps, mean_total, label="Average Total G-force", color="green")
plt.fill_between(steps, mean_total - std_total, mean_total + std_total,
                 alpha=0.3, color="green")


plt.title("Hybrid-based Total G-force Profile Across All Episodes")
plt.xlabel("Time Step", fontsize=10)
plt.ylabel("G-force (g)", fontsize=10)
plt.grid(True)
plt.legend(fontsize=9)
plt.tick_params(axis='both', which='major', labelsize=9)
plt.tight_layout()
plt.show()


