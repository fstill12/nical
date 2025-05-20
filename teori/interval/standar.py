from collections import namedtuple

# Namedtuple untuk konfigurasi warna
Config = namedtuple("Config", ["mayor", "minor", "dim", "aug"])

# Konstanta interval
mayor = [0, 4, 7]
minor = [0, 3, 7]
dim = [0, 3, 6]
aug = [0, 4, 8]

# Definisi warna
Interval = Config(mayor=mayor, minor=minor, dim=dim, aug=aug)
