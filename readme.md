# 🎹 Nical - Aplikasi CLI Pembuat Akor

**Nical** adalah aplikasi berbasis command-line interface (CLI) untuk membantu kamu membuat akor musik berdasarkan tuts dasar, jenis interval, dan notasi (#/b). Cocok untuk musisi, siswa teori musik, maupun developer musik digital.

---

## 📦 Instalasi

Pastikan kamu sudah menginstal Python dan pustaka `teori`.

```bash
pip install teori
```

---

## 🚀 Penggunaan

```bash
python nical.py -t TUTS -i INTERVAL -n NOTASI [--verbose]
```

### 🔧 Argumen

| Argumen      | Alias | Wajib    | Keterangan                                                  |
| ------------ | ----- | -------- | ----------------------------------------------------------- |
| `--tuts`     | `-t`  | ✅        | Tuts dasar, misal `C`, `D#`, `Bb`                           |
| `--interval` | `-i`  | ✅        | Jenis interval: `mayor`, `minor`, `diminished`, `augmented` |
| `--notasi`   | `-n`  | ✅        | Notasi nada: `sharp` (untuk `#`) atau `flat` (untuk `b`)    |
| `--verbose`  | `-v`  | opsional | Tampilkan akor lengkap dengan nama                          |

---

## 🧪 Contoh

### 1. Akor minor dari tuts D menggunakan notasi kres (`#`)

```bash
python nical.py -t D -i minor -n sharp
```

### 2. Akor mayor dari Bb dalam notasi mol (`b`) dengan hasil lengkap

```bash
python nical.py -t Bb -i mayor -n flat --verbose
```

---

## 🧠 Catatan

* Tuts bisa menggunakan `#` atau `b` (misal `F#`, `Eb`).
* Gunakan `--verbose` untuk melihat hasil akor disertai nama bentuknya.
* Program ini cocok untuk eksplorasi harmoni dasar dan susunan akor.

---

## 💡 Lisensi

MIT License © 2025

---

Jika kamu ingin, aku juga bisa bantu buat versi berbahasa Indonesia seluruhnya atau markdown dengan emoji dan hiasan CLI-style lainnya.
