from collections import namedtuple

# nama-nama tuts
NOTE_NAMES = ['C', 'C_Sharp', 'D', 'D_Sharp', 'E', 'F',
              'F_Sharp', 'G', 'G_Sharp', 'A', 'A_Sharp', 'B']

# Namedtuple untuk konfigurasi pola skala
Patterns = namedtuple("Patterns", NOTE_NAMES)

#definisi nilai
Tuts = Patterns(*NOTE_NAMES)

print(Tuts)
