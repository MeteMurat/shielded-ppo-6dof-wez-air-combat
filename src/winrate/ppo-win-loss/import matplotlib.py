import numpy as np
import matplotlib.pyplot as plt

# Dosyaların listesi
file_paths = [
    "C:/Users/90531/Desktop/win-loss/win_loss_tight0.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight1.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight2.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight3.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight4.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight5.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight6.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight7.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight8.npy",
    "C:/Users/90531/Desktop/win-loss/win_loss_tight9.npy"
]

# Tüm dosyalardan veriyi birleştirme C:\Users\90531\Desktop\win-loss
all_data = [np.load(file) for file in file_paths]
all_data = np.array(all_data)  # Çok boyutlu array
win = all_data[:, :, 0]
loss = all_data[:, :, 1]
tight = all_data[:, :, 2]

# Eğitim adımlarını ayarlama
steps = np.linspace(0, 3e4, win.shape[1])

# Grafikler için ortalama ve standart sapmayı hesaplama
win_mean, win_std = np.mean(win, axis=0), np.std(win, axis=0)
loss_mean, loss_std = np.mean(loss, axis=0), np.std(loss, axis=0)
tight_mean, tight_std = np.mean(tight, axis=0), np.std(tight, axis=0)

# Şekli ayırma
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Grafik 1: Sayılar (Number)
ax1.plot(steps, win_mean, color='red', label='Win (Mean)')
ax1.fill_between(steps, win_mean - win_std, win_mean + win_std, color='red', alpha=0.3)
ax1.plot(steps, loss_mean, color='green', label='Loss (Mean)')
ax1.fill_between(steps, loss_mean - loss_std, loss_mean + loss_std, color='green', alpha=0.3)
ax1.plot(steps, tight_mean, color='blue', label='Tie (Mean)')
ax1.fill_between(steps, tight_mean - tight_std, tight_mean + tight_std, color='blue', alpha=0.3)
ax1.set_xlabel('Train Step', fontsize=12)
ax1.set_ylabel('Number', fontsize=12)
ax1.legend()
ax1.grid(True)

# Grafik 2: Oranlar (Rate)
total = win_mean + loss_mean + tight_mean
ax2.plot(steps, win_mean / total * 100, color='red', label='Win Rate (Mean)')
ax2.fill_between(steps, (win_mean - win_std) / total * 100, (win_mean + win_std) / total * 100, color='red', alpha=0.3)
ax2.plot(steps, loss_mean / total * 100, color='green', label='Loss Rate (Mean)')
ax2.fill_between(steps, (loss_mean - loss_std) / total * 100, (loss_mean + loss_std) / total * 100, color='green', alpha=0.3)
ax2.plot(steps, tight_mean / total * 100, color='blue', label='Tie Rate (Mean)')
ax2.fill_between(steps, (tight_mean - tight_std) / total * 100, (tight_mean + tight_std) / total * 100, color='blue', alpha=0.3)
ax2.set_xlabel('Train Step', fontsize=12)
ax2.set_ylabel('Rate (%)', fontsize=12)
ax2.legend()
ax2.grid(True)

# Genel başlık ve gösterim
plt.tight_layout()
plt.show()
