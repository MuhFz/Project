# Project Akhir / UAS
## _Fitur awal_

### 1. Setup utama
- Konfigurasi Path untuk Library Tambahan Folder bernama [Image_Lib] ditambahkan ke [sys.path] , sehingga modul [image_utils] yang berada di folder tersebut bisa diakses.
- Import Modul [image_utils]
[image_utils] adalah modul eksternal, kemungkinan menyediakan utilitas tambahan untuk pengolahan citra.

### 2. Fungsi [image_resize]
Digunakan untuk mengubah ukuran gambar dengan menjaga aspek rasio, berdasarkan nilai width atau height yang diberikan:

- Jika _width_ atau _height_ tidak ditentukan (-1), aspek rasio tetap dijaga.
- Memanfaatkan fungsi cv2.resize.

### 3. SurfStitcher Class
kelas utama melakukan stitching panorama menggunakan SIFT dan homografi.
##### 1. inisialisasi(_init_)
 - membuat gambar awal (leftImage) dan parameter seperti rasio perbandingan deskripsi fitur (ratio) serta ambang batas reproyeksi (reprojThresh)
- Membuat objek detektor fitur SIFT (cv2.SIFT_create) dan matcher deskriptor (_BruteForce_).
- Memanggil fungsi _detectAndDescribe_ untuk mendeteksi fitur dan deskriptor pada gambar awal.

##### 2. Fungsi _detectAndDescribe_
- Mendapatkan keypoints (titik fitur penting) dan deskriptor menggunakan SIFT.
- Keypoints dikonversi ke array NumPy untuk mempermudah pemrosesan.

##### 3. Fungsi _Stitch_
Digunakan untuk menyusun gambar panorama:
- Gambar baru diubah menjadi grayscale.
- Keypoints dan deskriptor gambar baru dihitung.
- Fungsi getHomography dipanggil untuk menghitung matriks homografi antara gambar awal (leftImage) dan gambar baru.
- Jika homografi ditemukan, gambar baru diubah menggunakan cv2.warpPerspective sehingga cocok dengan gambar awal.
- Gambar hasil stitching disimpan sebagai gambar baru (_self.leftImage_) untuk iterasi berikutnya.

##### 4. Fungsi getHomography
Menghitung homografi dengan langkah:
- Membandingkan deskriptor gambar awal dan baru menggunakan metode KNN Matching.
- Memfilter hasil dengan ambang batas (ratio) untuk mendapatkan pasangan keypoints yang baik.
- Menggunakan RANSAC untuk menghitung homografi dari pasangan keypoints yang difilter.

##### 5. Fungsi _saveImage_
Menampilkan gambar akhir dan menyimpannya ke file jika diperlukan.

j

### Proses Output
Berikut adalah langkah utama yang menghasilkan output:
- Video atau kamera diproses frame demi frame.
- Setiap frame diolah menggunakan SIFT untuk mendeteksi fitur dan membangun homografi.
- Gambar baru disusun ke panorama dengan menggunakan matriks homografi.
- Panorama akhir ditampilkan di jendela GUI dan dapat disimpan ke file.

__Bagian selanjutnya adalah penjelasan yang berperan dalam menghasilkan output dari stitching gambar/ video menjadi panorama:__

## Inisialiasi dan Deteksi Fitur

Deteksi Fitur (SIFT): Fungsi cv2.SIFT_create digunakan untuk mendeteksi keypoints (titik fitur) dan deskriptor dari gambar. Fitur ini adalah dasar dari proses stitching, karena mencocokkan fitur antara dua gambar.

``` sh
self.surfFeature = cv2.SIFT_create(500)
self.matcher = cv2.DescriptorMatcher_create('BruteForce')

self.leftKps, self.leftDescriptor = self.detectAndDescribe(image)
````

Matcher: cv2.DescriptorMatcher_create('BruteForce') digunakan untuk mencocokkan deskriptor gambar secara brute force.

## Matching Fitur & Homografi
``` sh
rawMatches = self.matcher.knnMatch(self.leftDescriptor, rightDescriptor, 2)
matches = []

for m in rawMatches:
    if len(m) == 2 and m[0].distance < m[1].distance * self.ratio:
        matches.append((m[0].trainIdx, m[0].queryIdx))

if len(matches) >= 4:
    ptsB = np.float32([self.leftKps[i] for (_, i) in matches])
    ptsA = np.float32([rightKps[i] for (i, _) in matches])

    H, status = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, self.reprojThresh)
    return H

```
##### Explain
- Pencocokan Fitur: Menggunakan KNN (k-Nearest Neighbors) untuk mencocokkan deskriptor antara gambar pertama (self.leftDescriptor) dan gambar baru (rightDescriptor).
- Filter Rasio: Menerapkan rasio jarak Lowe untuk menghapus pasangan fitur yang kurang relevan.
- Homografi: Jika setidaknya ada 4 pasangan fitur yang valid, matriks homografi dihitung menggunakan metode RANSAC. Homografi adalah inti dari transformasi geometris dalam stitching.

## Transformasi & Penggabungan Gambar
``` sh
result = cv2.warpPerspective(image, H, (leftImageShape[1] + image.shape[1], image.shape[0]))
result[0:leftImageShape[0], 0:leftImageShape[1]] = self.leftImage

```

> Transformasi: cv2.warpPerspective menerapkan matriks homografi H untuk merubah gambar baru ke dalam perspektif gambar referensi.
Penggabungan: Gambar hasil transformasi digabungkan dengan gambar sebelumnya (self.leftImage) untuk membuat panorama.

## Loop Pengolahan Video
```sh
for i in range(3):
    for _ in range(10):
        grabbed, frame = camera.read()
    if not grabbed:
        break

    imageStitcher.stitch(frame)

```
> Loop ini membaca frame secara bertahap dari kamera/video dan memprosesnya untuk stitching.
> Frame yang diambil diproses dengan metode stitch, yang mencakup deteksi fitur, pencocokan, dan transformasi.

# Inti dari Program
> 1. __Deteksi Fitur (SIFT)__: Mengidentifikasi dan mendeskripsikan fitur penting dari gambar.
2. __Pencocokan Fitur__: Mencari pasangan fitur antara gambar-gambar yang akan digabung.
3. __Homografi__: Menghitung transformasi geometris untuk menyelaraskan gambar.
4. __Transformasi dan Penggabungan__: Menggunakan homografi untuk menggabungkan gambar menjadi panorama.
5. __Iterasi__: Mengulangi langkah di atas untuk setiap frame yang dibaca dari video/kamera.

### Output Hasil
![image](https://github.com/user-attachments/assets/8cf5beee-18ba-4e7c-88d1-803b16d3b01d)

![image](https://github.com/user-attachments/assets/a49bf948-f7a9-487a-9287-455c6a1a7f01)

