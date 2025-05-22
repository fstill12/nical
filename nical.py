import argparse
from teori import achord, Note
from teori.interval import mayor, minor, diminished, augmented
import re

def is_valid_str(tuts: str) -> bool:
    """Validasi format tuts: huruf A–G diikuti opsional '#' atau 'b'."""
    return bool(re.fullmatch(r"[A-Ga-g]+", tuts))

def validate_tuts(tuts: str) -> str | None:
    """Validasi argumen tuts dan berikan pesan error jika ada masalah."""
    if tuts is None:
        return "Kesalahan: perintah --tuts atau -t belum diberikan."
    if not tuts.isalpha():
        return "Kesalahan: Input tidak boleh mengandung angka atau karakter tidak valid."
    if not is_valid_str(tuts):
        return "Kesalahan: Input hanya boleh berupa A–G."
    return None

def get_qualitas(args) -> str | None:
    """Dapatkan interval kualitas berdasarkan argumen."""
    qualitas = [args.mayor, args.minor, args.diminished, args.augmented]
    if any(qualitas):
        return qualitas
    return None

def get_notasi(args) -> str | None:
    """Dapatkan notasi berdasarkan argumen."""
    if args.sharp:
        return "sharp"
    if args.flat:
        return "flat"
    return None

def validate_args(args) -> str | None:
    """Validasi interval dan notasi, kembalikan pesan error jika perlu."""
    if get_qualitas(args) is None:
        return "Kesalahan: Pilih salah satu interval --minor (-m), --mayor (-M), --diminished (-dim) atau --augmented (-aug)."
    if get_notasi(args) is None:
        return "Kesalahan: Pilih salah satu notasi --sharp (-s) atau --flat (-f)."
    return None

def run(args: argparse.Namespace):
    # Validasi tuts
    error = validate_tuts(args.tuts)
    if error:
        print(error)
        return

    # Validasi interval dan notasi
    error = validate_args(args)
    if error:
        print(error)
        return

    # Ambil parameter yang sudah pasti valid
    kunci = args.tuts.title()
    dval = [ a for a, b in enumerate(get_qualitas(args)) if b == True ]
    print(dval)
    interval = [mayor.simbol["mayor"], minor.simbol["minor"], diminished.simbol["diminished"], augmented.simbol["augmented"]]
    jval = [mayor.simbol["title"], minor.simbol["title"], diminished.simbol["title"], augmented.simbol["title"]]
    n = Note.sharp if args.sharp else Note.flat
    for i in dval:
        print()
        print(f"tangga nada {jval[i]}".title())
        print()
        for x, y in interval[i].items():
            hasil = achord(note=n, tuts=kunci, q=y)
            if args.verbose:
                print(f"akor {x.replace("C", kunci)} = {hasil}")
            else:
                print(hasil)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Nical", description="Nical aplikasi membuat akor", allow_abbrev=False)
    parser.add_argument('--tuts', '-t', type=str, help="Jenis tuts (misal: C, D#, Bb)")
    parser.add_argument('--verbose', '-v', action="store_true", help="Tampilkan hasil secara lengkap")
    parser.add_argument('--mayor', '-M', action="store_true", help="Gunakan akor mayor")
    parser.add_argument('--minor', '-m', action="store_true", help="Gunakan akor minor")
    parser.add_argument('--diminished', '-dim', action="store_true", help="Gunakan akor diminished")
    parser.add_argument('--augmented', '-aug', action="store_true", help="Gunakan akor augmented")
    parser.add_argument('--sharp', '-s', action="store_true", help="Gunakan notasi dengan # (kres)")
    parser.add_argument('--flat', '-f', action="store_true", help="Gunakan notasi dengan b (mol)")
    parser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)
