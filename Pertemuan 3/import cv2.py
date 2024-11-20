Pertemuan Tiga

import cv2
import matplotlib.pyplot as plt

# Membaca citra dari file
image = cv2.imread('c:\Users\HP\OneDrive\Documents\OneDrive\Pictures\11233056625_208e41615f_k.jpg')

# Mengubah citra dari BGR ke RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Mengubah citra ke grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mengubah citra ke HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Mengubah citra ke hitam-putih (BW) menggunakan threshold
_, image_bw = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

# Menampilkan citra menggunakan matplotlib
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].imshow(image_rgb)
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')

axes[0, 1].imshow(image_gray, cmap='gray')
axes[0, 1].set_title('Grayscale')
axes[0, 1].axis('off')

axes[1, 0].imshow(image_hsv[..., 0], cmap='hsv')  # Menampilkan kanal Hue
axes[1, 0].set_title('HSV Hue')
axes[1, 0].axis('off')

axes[1, 1].imshow(image_bw, cmap='gray')
axes[1, 1].set_title('Black & White')
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()
