from collections import namedtuple

# Namedtuple untuk konfigurasi warna
Config = namedtuple("Config", ["mayor", "minor"])

# Konstanta interval
mayor = [0, 4, 7]
minor = [0, 3, 7]

# Definisi warna
Interval = Config(mayor=mayor, minor=minor)
