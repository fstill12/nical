from collections import namedtuple

# Namedtuple untuk konfigurasi config
Config = namedtuple("Config", 
                    [
                        "flat", "sharp", "tangga_nada", "derajat",
                        "stn", "quality"])

# Namedtuple untuk konfigurasi config
Skala = namedtuple("Skala", ["mayor", "minor"])

# Konstanta flat
flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

# Konstanta flat
sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Degree dan kualitas akor pada tangga nada mayor
skala_diatonik_mayor = {
    "judul": "mayor",
    "tangga_nada": {
        'I': 'major',
        'ii': 'minor',
        'iii': 'minor',
        'IV': 'major',
        'V': 'major',
        'vi': 'minor',
        'vii°': 'diminished'}
    }
    

# Degree dan kualitas akor pada tangga nada minor alami
skala_diatonik_minor = {
    "judul": "minor",
    "tangga_nada": {
        'i': 'minor',
        'ii°': 'diminished',
        'III': 'major',
        'iv': 'minor',
        'v': 'minor',
        'VI': 'major',
        'VII': 'major'} 
    }
    

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

# simbol tangga nada mayor dan minor
simbol_tangga_nada = {
    "mayor": "",
    "major": "",
    "minor": "m",
    "diminished": "dim",
    "augmented": "aug"
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

# Definisi kunci relatif untuk mode
# diambil dari kode usmber pychord
# https://en.wikipedia.org/wiki/Mode_(music)#Modern_modes
# Ionian -> maj, Aeolian -> min
RELATIVE_KEY_DICT = {
    'maj': [0, 2, 4, 5, 7, 9, 11, 12],
    'Dor': [0, 2, 3, 5, 7, 9, 10, 12],
    'Phr': [0, 1, 3, 5, 7, 8, 10, 12],
    'Lyd': [0, 2, 4, 6, 7, 9, 11, 12],
    'Mix': [0, 2, 4, 5, 7, 9, 10, 12],
    'min': [0, 2, 3, 5, 7, 8, 10, 12],
    'Loc': [0, 1, 3, 5, 6, 8, 10, 12],
}

# Kualitas akor yang umum digunakan
# diambil dari kode usmber pychord
DEFAULT_QUALITIES = [
    # 2 notes
    ('5', (0, 7)),
    ('no5', (0, 4)),
    ('omit5', (0, 4)),
    ('min(no5)', (0, 3)),
    ('min(omit5)', (0, 3)),
    # 3 notes
    ('maj', (0, 4, 7)),
    ('min', (0, 3, 7)),
    ('dim', (0, 3, 6)),
    ('aug', (0, 4, 8)),
    ('sus2', (0, 2, 7)),
    ('sus4', (0, 5, 7)),
    # 4 notes
    ('maj6', (0, 4, 7, 9)),
    ('min6', (0, 3, 7, 9)),
    ('maj7', (0, 4, 7, 11)),
    ('min7', (0, 3, 7, 10)),
    ('dim7', (0, 3, 6, 9)),
    ('aug7', (0, 4, 8, 10)),
    ('7', (0, 4, 7, 10)),
    ('min7b5', (0, 3, 6, 10)),
    ('sus4add9', (0, 5, 7, 14)),
    ('sus4add2', (0, 2, 5, 7)),
    # 5 notes
    ('maj9', (0, 4, 7, 11, 14)),
    ('min9', (0, 3, 7, 10, 14)),
    ('9', (0, 4, 7, 10, 14)),
    ('dim9', (0, 3, 6, 9, 14)),
    ('aug9', (0, 4, 8, 10, 14)),
    ('maj11', (0, 4, 7, 11, 14, 17)),
    ('min11', (0, 3, 7, 10, 14, 17)),
    ('11', (0, 7, 10, 14, 17)),
    ('maj13', (0, 4, 7, 11, 14, 21)),
    ('min13', (0, 3, 7, 10, 14, 21)),
    ('13', (0, 4, 7, 10, 14, 21)),
    # add chords
    ('add9', (0, 4, 7, 14)),
    ('minadd9', (0, 3, 7, 14)),
    ('majadd9', (0, 4, 7, 14)),
    ('add11', (0, 4, 7, 17)),
    ('minadd11', (0, 3, 7, 17)),
    ('majadd11', (0, 4, 7, 17)),
    # sus chords
    ('sus', (0, 5, 7)),
    # alternatives (for compatibility)
    ('m', (0, 3, 7)),  # minor
    ('M', (0, 4, 7)),  # major
]

# Definisi konfigurasi untuk tangga nada
Note = Config(flat=flat, sharp=sharp, tangga_nada=rumus, 
              derajat=derajat, stn=simbol_tangga_nada, quality=DEFAULT_QUALITIES)
# Definisi skala diatonik mayor dan minor
Diatonik = Skala(mayor=skala_diatonik_mayor, minor=skala_diatonik_minor)