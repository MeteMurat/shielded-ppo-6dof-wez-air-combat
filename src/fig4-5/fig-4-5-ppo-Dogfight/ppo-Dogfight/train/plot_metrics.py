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
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('ATA (°)')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(t, distance, 'k--', label='Distance')
ax2.set_ylabel('Distance (km)')
ax2.legend(loc='upper right')

plt.title('Figure 4(b): ATA and Distance vs Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Şekil 4(c): Mach ve Yükseklik ---
fig, ax1 = plt.subplots()
ax1.plot(t, mach_red, 'r-', label='Mach Red')
ax1.plot(t, mach_blue, 'b-', label='Mach Blue')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Mach')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(t, h_red, 'r--', label='Height Red')
ax2.plot(t, h_blue, 'b--', label='Height Blue')
ax2.set_ylabel('Height (km)')
ax2.legend(loc='upper right')

plt.title('Figure 4(c): Mach and Altitude vs Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Şekil 5(d): Sadece Yükseklik Karşılaştırması ---
plt.figure()
plt.plot(t, h_red, 'r-', label='Red Height')
plt.plot(t, h_blue, 'b-', label='Blue Height')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (km)')
plt.title('Figure 5(d): Altitude Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
