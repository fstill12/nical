from collections import namedtuple

# Namedtuple untuk konfigurasi warna
Config = namedtuple("Config", ["flat", "sharp"])

# Konstanta flat
flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

# Konstanta flat
sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Definisi warna
Note = Config(flat=flat, sharp=sharp)