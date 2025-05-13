from collections import namedtuple

# nama - nama derajat
DEGREE_NAMES = {
    1: "1 (tonik)",
    2: "2 (supertonik)",
    3: "3 (mediant)",
    4: "4 (subdominant)",
    5: "5 (dominant)",
    6: "6 (submediant)",
    7: "7 (leading tone/subtonik)",
}

# Namedtuple untuk konfigurasi pola skala
Patterns = namedtuple("Patterns", [*DEGREE_NAMES])

#definisi nilai
DEGREE = Patterns(*DEGREE_NAMES.values())
