import argparse

NOTE_LIST_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
NOTE_LIST_FLAT =  ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

CHORD_PATTERNS = {
    "mayor": [0, 4, 7],
    "minor": [0, 3, 7],
    "diminished": [0, 3, 6],
    "augmented": [0, 4, 8]
}

ROMAN_NUMERALS = {
    "I": 0, "II": 2, "III": 4, "IV": 5, "V": 7, "VI": 9, "VII": 11
}

CHORDS_MAJOR = ["mayor", "minor", "minor", "mayor", "mayor", "minor", "diminished"]

def identify_chord(notes):
    try:
        semitones = sorted([NOTE_LIST_SHARP.index(n) for n in notes])
    except ValueError:
        return "Nada tidak valid."

    for root in notes:
        idx_root = NOTE_LIST_SHARP.index(root)
        intervals = sorted([(NOTE_LIST_SHARP.index(n) - idx_root) % 12 for n in notes])
        for nama, pola in CHORD_PATTERNS.items():
            if intervals == sorted(pola):
                return f"{root} {nama}"
    return "Akor tidak ditemukan."

def generate_progression(key, pattern, use_sharp=True):
    note_list = NOTE_LIST_SHARP if use_sharp else NOTE_LIST_FLAT
    if key not in note_list:
        return [f"Key '{key}' tidak valid"]
    
    idx = note_list.index(key)
    scale = [(note_list[(idx + x) % 12]) for x in [0, 2, 4, 5, 7, 9, 11]]
    
    result = []
    for roman in pattern.upper().split('-'):
        if roman in ROMAN_NUMERALS:
            posisi = list(ROMAN_NUMERALS.keys()).index(roman)
            chord = scale[posisi] + f" ({CHORDS_MAJOR[posisi]})"
            result.append(chord)
        else:
            result.append(f"? ({roman})")
    return result

def generate_chord(root, chord_type, use_sharp=True):
    pattern = CHORD_PATTERNS.get(chord_type.lower())
    if not pattern:
        return f"Tipe akor '{chord_type}' tidak dikenali"
    
    note_list = NOTE_LIST_SHARP if use_sharp else NOTE_LIST_FLAT
    if root not in note_list:
        return f"Akar nada '{root}' tidak valid"

    idx = note_list.index(root)
    return [note_list[(idx + p) % 12] for p in pattern]

def main():
    parser = argparse.ArgumentParser(description="Aplikasi Pengolah Akor")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: chord
    chord_parser = subparsers.add_parser("chord", help="Deteksi nama akor dari nada-nada")
    chord_parser.add_argument("--notes", nargs="+", required=True)

    # Subcommand: progression
    prog_parser = subparsers.add_parser("progression", help="Buat progresi akor dari key dan pola")
    prog_parser.add_argument("--key", required=True)
    prog_parser.add_argument("--pattern", required=True)

    # Subcommand: generate
    gen_parser = subparsers.add_parser("generate", help="Buat akor dari root dan jenis")
    gen_parser.add_argument("--root", required=True)
    gen_parser.add_argument("--type", required=True)
    gen_parser.add_argument("--notasi", default="angka", choices=["angka", "latin"])
    gen_parser.add_argument("--tanda", default="kres", choices=["kres", "mol"])
    gen_parser.add_argument("--output", default="terminal")

    args = parser.parse_args()

    if args.command == "chord":
        print("Identifikasi Akor:")
        hasil = identify_chord(args.notes)
        print(hasil)

    elif args.command == "progression":
        hasil = generate_progression(args.key, args.pattern)
        print("Progressi Akor:")
        print(" - ".join(hasil))

    elif args.command == "generate":
        use_sharp = args.tanda == "kres"
        hasil = generate_chord(args.root, args.type, use_sharp)
        print(f"Akor {args.root} {args.type}:")
        print("Nada: " + ", ".join(hasil))

if __name__ == "__main__":
    main()
