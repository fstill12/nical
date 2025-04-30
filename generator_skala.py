# Skala dasar dengan interval (dalam jumlah langkah setengah nada)
SCALE_PATTERNS = {
    "major": [2, 2, 1, 2, 2, 2, 1],
    "minor": [2, 1, 2, 2, 1, 2, 2],
    "harmonic minor": [2, 1, 2, 2, 1, 3, 1],
    "melodic minor": [2, 1, 2, 2, 2, 2, 1],
    "major pentatonic": [2, 2, 3, 2, 3],
    "minor pentatonic": [3, 2, 2, 3, 2],
    "blues": [3, 2, 1, 1, 3, 2],
    "chromatic": [1] * 12,
    "whole tone": [2] * 6
}

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F',
              'F#', 'G', 'G#', 'A', 'A#', 'B']

DEGREE_NAMES = {
    1: "1 (tonik)",
    2: "2 (supertonik)",
    3: "3 (mediant)",
    4: "4 (subdominant)",
    5: "5 (dominant)",
    6: "6 (submediant)",
    7: "7 (leading tone/subtonik)",
}

def get_scale(root, scale_type):
    root = root.capitalize()
    if root not in NOTE_NAMES:
        raise ValueError(f"Nada {root} tidak valid.")
    
    intervals = SCALE_PATTERNS.get(scale_type.lower())
    if not intervals:
        raise ValueError(f"Skala '{scale_type}' tidak dikenali.")
    
    start_index = NOTE_NAMES.index(root)
    scale_notes = [root]
    idx = start_index

    for step in intervals:
        idx = (idx + step) % 12
        scale_notes.append(NOTE_NAMES[idx])
    
    return scale_notes

def label_degrees(scale_notes):
    degree_labels = []
    for i, note in enumerate(scale_notes[:-1]):  # exclude octave
        degree = (i + 1)
        label = DEGREE_NAMES.get(degree, f"{degree}")
        degree_labels.append(f"{note} = {label}")
    return degree_labels

# Contoh penggunaan
if __name__ == "__main__":
    root_note = input("Masukkan nada dasar (misalnya C, A, F#): ").strip()
    scale_type = input("Masukkan jenis skala (major, minor, blues, dll): ").strip()

    try:
        notes = get_scale(root_note, scale_type)
        print(f"\nSkala {root_note} {scale_type}:\n{' - '.join(notes)}")
        print("\nNilai setiap nada dalam skala:")
        for label in label_degrees(notes):
            print(label)
    except ValueError as e:
        print("Error:", e)
