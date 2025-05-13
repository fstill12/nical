from collections import namedtuple

# Skala dasar dengan interval (dalam jumlah langkah setengah nada)
SCALE_PATTERNS = {
    "major": [2, 2, 1, 2, 2, 2, 1],
    "minor": [2, 1, 2, 2, 1, 2, 2],
    "harmonic_minor": [2, 1, 2, 2, 1, 3, 1],
    "melodic_minor": [2, 1, 2, 2, 2, 2, 1],
    "major_pentatonic": [2, 2, 3, 2, 3],
    "minor_pentatonic": [3, 2, 2, 3, 2],
    "blues": [3, 2, 1, 1, 3, 2],
    "chromatic": [1] * 12,
    "whole_tone": [2] * 6
}

# Namedtuple untuk konfigurasi pola skala
Patterns = namedtuple("Patterns", [*SCALE_PATTERNS])

#definisi nilai
Scale = Patterns(*SCALE_PATTERNS.values())
