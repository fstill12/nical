import argparse

# Membuat objek parser
parser = argparse.ArgumentParser(description="Contoh program parser argumen")

# Menambahkan argumen yang dapat diterima
parser.add_argument('--nama', type=str, help="Nama pengguna")
parser.add_argument('--umur', type=int, help="Umur pengguna")
parser.add_argument('--kota', type=str, help="Kota tempat tinggal", default="Tidak diketahui")

# Mengurai argumen yang diberikan
args = parser.parse_args()

# Menampilkan hasil
print(f"Nama: {args.nama}")
print(f"Umur: {args.umur}")
print(f"Kota: {args.kota}")
