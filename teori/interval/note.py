from collections import namedtuple

# Namedtuple untuk konfigurasi warna
Config = namedtuple("Config", ["flat", "sharp", "tangga_nada", "derajat"])

# Konstanta flat
flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

# Konstanta flat
sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Rumus tangga nada
rumus = {
    "judul": "rumus_interval_tangga_nada",
    "tangga_nada":{
        "mayor": [2, 2, 1, 2, 2, 2, 1],
        "mayor_pentatonik": [2, 2, 3, 2, 3],
        "minor": [2, 1, 2, 2, 1, 2, 2],
        "minor_harmonik": [2, 1, 2, 2, 1, 3, 1],
        "minor_melodik": [2, 1, 2, 2, 2, 2, 1],
        "minor_pentatonik": [3, 2, 2, 3, 2],
        "blues": [3, 2, 1, 1, 3, 2],
        "kromatik": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "whole_tone": [2, 2, 2, 2, 2, 2],
    } 
}

# Definisi derajat tangga nada
derajat = {
    1: "1 (tonik)",
    2: "2 (supertonik)",
    3: "3 (mediant)",
    4: "4 (subdominant)",
    5: "5 (dominant)",
    6: "6 (submediant)",
    7: "7 (leading tone/subtonik)",
}

# Definisi warna
Note = Config(flat=flat, sharp=sharp, tangga_nada=rumus, derajat=derajat)