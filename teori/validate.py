import re

# universal validasi dan konversi tuts
def convert_tuts_to_notasi(tuts: str, notasi: str) -> str:
    """Konversi tuts ke notasi yang sesuai (sharp/flat)."""
    sharp_to_flat = {
        "C#": "Db", "D#": "Eb", "F#": "Gb", "G#": "Ab", "A#": "Bb"
    }
    flat_to_sharp = {v: k for k, v in sharp_to_flat.items()}
    tuts = tuts.title()
    if notasi == "flat" and tuts in sharp_to_flat:
        return sharp_to_flat[tuts]
    if notasi == "sharp" and tuts in flat_to_sharp:
        return flat_to_sharp[tuts]
    return tuts

def is_valid_str(tuts: str) -> bool:
    """Cek apakah input tuts valid."""
    return bool(re.fullmatch(r"[A-Ga-g][#b]?", tuts))

def is_valid_akor(tuts: str) -> bool:
    """Cek apakah input adalah akor."""
    return re.fullmatch(r"\b[A-Ga-g][#b]?\b", tuts)

def validate_tuts(tuts: str) -> str | None:
    """Validasi input tuts."""
    if tuts is None:
        return "Kesalahan: perintah --tuts belum diberikan."
    if not is_valid_str(tuts):
        return "Kesalahan: Input hanya boleh berupa huruf A–G diikuti opsional '#' atau 'b'."
    return None