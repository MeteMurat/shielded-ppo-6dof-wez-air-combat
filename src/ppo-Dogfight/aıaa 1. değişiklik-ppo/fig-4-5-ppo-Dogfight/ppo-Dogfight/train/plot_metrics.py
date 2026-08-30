import numpy as np
import matplotlib.pyplot as plt
import os

# --- Bu script çalıştığı dizinde Record klasörlerinden veri çeker ---
record_index = 5  # En başarılı Record5
episode = 1       # İlgili ep numarası (kayıtlı dosya numarası)

folder = f"Record{record_index}"

def load_array(name):
    path = os.path.join(folder, f"{name}_ep{episode}.npy")
    return np.load(path)

# Verileri yükle
ata_red = load_array("ATA_red")
ata_blue = load_array("ATA_blue")
distance = load_array("distance")
mach_red = load_array("mach_red")
mach_blue = load_array("mach_blue")
h_red = load_array("height_red")
h_blue = load_array("height_blue")

# Zaman vektörü oluştur (100 step * 0.01s * adım sayısı)
t = np.linspace(0, len(ata_red)*0.01, len(ata_red))

# --- Şekil 4(b): ATA ve Mesafe ---
fig, ax1 = plt.subplots()
ax1.plot(t, ata_red, 'r-', label='ATA Red')
ax1.plot(t, ata_blue, 'b-', label='ATA Blue')
ax1.set_xlabel('Time (s)', fontsize=10)
ax1.set_ylabel('ATA (°)', fontsize=10)
ax1.tick_params(axis='both', labelsize=9)
ax1.legend(loc='upper left', fontsize=9)

ax2 = ax1.twinx()
ax2.plot(t, distance, 'k--', label='Distance')
ax2.set_ylabel('Distance (km)', fontsize=10)
ax2.tick_params(axis='y', labelsize=9)
ax2.legend(loc='upper right', fontsize=9)

plt.title('ATA and Distance vs Time for PPO Simulation', fontsize=11)
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Şekil 4(c): Mach ve Yükseklik ---
fig, ax1 = plt.subplots()
ax1.plot(t, mach_red, 'r-', label='Mach Red')
ax1.plot(t, mach_blue, 'b-', label='Mach Blue')
ax1.set_xlabel('Time (s)', fontsize=10)
ax1.set_ylabel('Mach', fontsize=10)
ax1.tick_params(axis='both', labelsize=9)
ax1.legend(loc='upper left', fontsize=9)


ax2 = ax1.twinx()
ax2.plot(t, h_red, 'r--', label='Height Red')
ax2.plot(t, h_blue, 'b--', label='Height Blue')
ax2.set_ylabel('Height (km)', fontsize=10)
ax2.tick_params(axis='y', labelsize=9)
ax2.legend(loc='upper right', fontsize=9)

plt.title('Mach and Altitude vs Time for PPO Simulation', fontsize=11)
plt.grid(True)
plt.tight_layout()
plt.show()

