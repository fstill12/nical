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
    # chords consist of 2 notes
    ('5', (0, 7)),
    ('no5', (0, 4)),
    ('omit5', (0, 4)),
    ('m(no5)', (0, 3)),
    ('m(omit5)', (0, 3)),
    # 3 notes
    ('', (0, 4, 7)),
    ('maj', (0, 4, 7)),
    ('m', (0, 3, 7)),
    ('min', (0, 3, 7)),
    ('-', (0, 3, 7)),
    ('dim', (0, 3, 6)),
    # Not to confuse Ab5 with A(b5)
    ('(b5)', (0, 4, 6)),
    ('aug', (0, 4, 8)),
    ('sus2', (0, 2, 7)),
    ('sus4', (0, 5, 7)),
    ('sus', (0, 5, 7)),
    # 4 notes
    ('6', (0, 4, 7, 9)),
    ('6b5', (0, 4, 6, 9)),  # https://www.scales-chords.com/chord/piano/C%236b5
    ('6-5', (0, 4, 6, 9)),  # https://www.scales-chords.com/chord/piano/C%236b5
    ('7', (0, 4, 7, 10)),
    ('7-5', (0, 4, 6, 10)),
    ('7b5', (0, 4, 6, 10)),
    ('7+5', (0, 4, 8, 10)),
    ('7#5', (0, 4, 8, 10)),
    ('7sus4', (0, 5, 7, 10)),
    ('m6', (0, 3, 7, 9)),
    ('m7', (0, 3, 7, 10)),
    ('m7-5', (0, 3, 6, 10)),
    ('m7b5', (0, 3, 6, 10)),
    ('m7+5', (0, 3, 8, 10)),
    ('m7#5', (0, 3, 8, 10)),
    ('dim6', (0, 3, 6, 8)),
    ('dim7', (0, 3, 6, 9)),
    ('M7', (0, 4, 7, 11)),
    ('maj7', (0, 4, 7, 11)),
    ('maj7+5', (0, 4, 8, 11)),
    ('M7+5', (0, 4, 8, 11)),
    ('mmaj7', (0, 3, 7, 11)),
    ('mM7', (0, 3, 7, 11)),
    ('add4', (0, 4, 5, 7)),
    ('majadd4', (0, 4, 5, 7)),
    ('Madd4', (0, 4, 5, 7)),
    ('madd4', (0, 3, 5, 7)),
    ('add9', (0, 4, 7, 14)),
    ('majadd9', (0, 4, 7, 14)),
    ('Madd9', (0, 4, 7, 14)),
    ('madd9', (0, 3, 7, 14)),
    ('sus4add9', (0, 5, 7, 14)),
    ('sus4add2', (0, 2, 5, 7)),
    ('2', (0, 4, 7, 14)),
    ('add11', (0, 4, 7, 17)),
    ('4', (0, 4, 7, 17)),
    # 5 notes
    ('m69', (0, 3, 7, 9, 14)),
    ('69', (0, 4, 7, 9, 14)),
    ('9', (0, 4, 7, 10, 14)),
    ('m9', (0, 3, 7, 10, 14)),
    ('M9', (0, 4, 7, 11, 14)),
    ('maj9', (0, 4, 7, 11, 14)),
    ('9sus4', (0, 5, 7, 10, 14)),
    ('7-9', (0, 4, 7, 10, 13)),
    ('7b9', (0, 4, 7, 10, 13)),
    ('7(b9)', (0, 4, 7, 10, 13)),   # https://www.oolimo.com/guitarchords/Fsharp7(b9)
    ('7+9', (0, 4, 7, 10, 15)),
    ('7#9', (0, 4, 7, 10, 15)),
    ('9-5', (0, 4, 6, 10, 14)),
    ('9b5', (0, 4, 6, 10, 14)),
    ('9+5', (0, 4, 8, 10, 14)),
    ('9#5', (0, 4, 8, 10, 14)),
    ('7#9b5', (0, 4, 6, 10, 15)),
    ('7#9#5', (0, 4, 8, 10, 15)),
    ('m7b9b5', (0, 3, 6, 10, 13)),
    ('7b9b5', (0, 4, 6, 10, 13)),
    ('7b9#5', (0, 4, 8, 10, 13)),
    ('11', (0, 7, 10, 14, 17)),
    ('7+11', (0, 4, 7, 10, 18)),
    ('7#11', (0, 4, 7, 10, 18)),
    ('maj7+11', (0, 4, 7, 11, 18)),
    ('M7+11', (0, 4, 7, 11, 18)),
    ('maj7#11', (0, 4, 7, 11, 18)),
    ('M7#11', (0, 4, 7, 11, 18)),
    ('7b9#9', (0, 4, 7, 10, 13, 15)),
    ('7b9#11', (0, 4, 7, 10, 13, 18)),
    ('7#9#11', (0, 4, 7, 10, 15, 18)),
    ('7-13', (0, 4, 7, 10, 20)),
    ('7b13', (0, 4, 7, 10, 20)),
    ('m7add11', (0, 3, 7, 10, 17)),
    ('maj7add11', (0, 4, 7, 11, 17)),
    ('M7add11', (0, 4, 7, 11, 17)),
    ('mmaj7add11', (0, 3, 7, 11, 17)),
    ('mM7add11', (0, 3, 7, 11, 17)),
    # 6 notes
    ('7b9b13', (0, 4, 7, 10, 13, 17, 20)),
    ('9+11', (0, 4, 7, 10, 14, 18)),
    ('9#11', (0, 4, 7, 10, 14, 18)),
    ('m11', (0, 3, 7, 10, 14, 17)),    # https://chord-c.com/guitar-chord/B/minor-eleventh/
    ('13', (0, 4, 7, 10, 14, 21)),
    ('13-9', (0, 4, 7, 10, 13, 21)),
    ('13b9', (0, 4, 7, 10, 13, 21)),
    ('13+9', (0, 4, 7, 10, 15, 21)),
    ('13#9', (0, 4, 7, 10, 15, 21)),
    ('13+11', (0, 4, 7, 10, 18, 21)),
    ('13#11', (0, 4, 7, 10, 18, 21)),
    ('maj13', (0, 4, 7, 11, 14, 21)),   # https://chord-c.com/guitar-chord/C/major-thirteenth/
    ('M13', (0, 4, 7, 11, 14, 21)),
    ('maj7add13', (0, 4, 7, 9, 11, 14)),
    ('M7add13', (0, 4, 7, 9, 11, 14)),
]

# Definisi konfigurasi untuk tangga nada
Note = Config(flat=flat, sharp=sharp, tangga_nada=rumus, 
              derajat=derajat, stn=simbol_tangga_nada, quality=DEFAULT_QUALITIES)
# Definisi skala diatonik mayor dan minor
Diatonik = Skala(mayor=skala_diatonik_mayor, minor=skala_diatonik_minor)