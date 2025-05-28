from collections import namedtuple

# Namedtuple untuk konfigurasi warna
Config = namedtuple("Config", ["flat", "sharp", "tangga_nada"])

# Konstanta flat
flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

# Konstanta flat
sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

rumus = {
    "judul": "rumus_interval_tangga_nada",
    "tangga_nada":{
        "mayor": [2, 2, 1, 2, 2, 2, 1],
        "minor": [2, 1, 2, 2, 1, 2, 2],
        "minor_natural": [2, 1, 2, 2, 1, 2, 2],
        "minor_harmonik": [2, 1, 2, 2, 1, 3, 1],
        "minor_melodik": [2, 1, 2, 2, 2, 2, 1],
        "kromatik": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    } 
}

# Definisi warna
Note = Config(flat=flat, sharp=sharp, tangga_nada=rumus)