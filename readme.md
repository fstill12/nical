# 🎹 Nical - Aplikasi CLI Pembuat Akor Musik

**Nical** adalah aplikasi berbasis antarmuka baris perintah (CLI) untuk membantu kamu membuat akor musik berdasarkan tuts dasar, jenis interval, dan notasi (#/b). Cocok untuk musisi, pelajar teori musik, maupun developer musik digital.

---

## 📦 Instalasi

Pastikan kamu sudah menginstal Python dan pustaka `teori` terlebih dahulu:

```bash
pip install teori
```

---

## 🚀 Cara Penggunaan

```bash
python nical.py <perintah> [opsi...]
```

### ✅ Perintah Utama yang Tersedia

#### 🎼 `chord` – Buat akor berdasarkan tuts

```bash
python nical.py chord -t TUTS -i INTERVAL -n NOTASI [--verbose]
```

| Argumen      | Alias | Wajib    | Keterangan                                                       |
| ------------ | ----- | -------- | ---------------------------------------------------------------- |
| `--tuts`     | `-t`  | ✅        | Tuts dasar, misalnya `C`, `D#`, `Bb`                             |
| `--interval` | `-i`  | ✅        | Jenis interval akor: `mayor`, `minor`, `diminished`, `augmented` |
| `--notasi`   | `-n`  | ✅        | Jenis notasi: `sharp` (untuk `#`) atau `flat` (untuk `b`)        |
| `--verbose`  | `-v`  | opsional | Tampilkan hasil akor lengkap dengan nama bentuk akor             |

📌 *Gunakan `--verbose` untuk menampilkan bentuk dan nama akor yang lebih detail.*

---

## 🧪 Contoh Penggunaan

### 1. Menampilkan akor **minor** dari tuts **D** dengan notasi kres (`#`):

```bash
python nical.py chord -t D -i minor -n sharp
```

### 2. Menampilkan akor **mayor** dari tuts **Bb** dengan notasi mol (`b`) dan hasil lengkap:

```bash
python nical.py chord -t Bb -i mayor -n flat --verbose
```

---

### 🚧 Perintah Lain (Dalam Pengembangan)

| Perintah  | Status         | Keterangan                                               |
| --------- | -------------- | -------------------------------------------------------- |
| `scale`   | 🔧 Akan datang | Tangga nada berdasarkan tuts dan jenis skala             |
| `analyze` | 🔧 Akan datang | Analisis akor dari input                                 |
| `suggest` | 🔧 Akan datang | Rekomendasi progresi akor yang cocok berdasarkan konteks |

📭 *Perintah-perintah di atas akan tersedia dalam versi mendatang. Nantikan pembaruannya!*

---

## 💡 Catatan Tambahan

* Input `tuts` hanya boleh terdiri dari huruf `A`–`G` disertai opsional `#` atau `b`.
* Aplikasi cocok untuk eksplorasi harmoni dan belajar teori musik dasar.
* Cocok digunakan untuk pelajar maupun musisi digital.

---

## 📜 Lisensi

MIT License © 2025