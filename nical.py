import argparse
from teori import achord, Interval, Note
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
    if args.minor:
        return "minor"
    if args.mayor:
        return "mayor"
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
        return "Kesalahan: Pilih salah satu interval --minor (-m) atau --mayor (-M)."
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
    q = Interval.minor if args.minor else Interval.mayor
    n = Note.sharp if args.sharp else Note.flat

    hasil = achord(note=n, tuts=kunci, q=q)
    if args.verbose:
        print(f"akor {kunci} = {hasil}")
    else:
        print(hasil)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Nical", description="Nical aplikasi membuat akor", allow_abbrev=False)
    parser.add_argument('--tuts', '-t', type=str, help="Jenis tuts (misal: C, D#, Bb)")
    parser.add_argument('--verbose', '-v', action="store_true", help="Tampilkan hasil secara lengkap")
    parser.add_argument('--mayor', '-M', action="store_true", help="Gunakan akor mayor")
    parser.add_argument('--minor', '-m', action="store_true", help="Gunakan akor minor")
    parser.add_argument('--sharp', '-s', action="store_true", help="Gunakan notasi dengan # (kres)")
    parser.add_argument('--flat', '-f', action="store_true", help="Gunakan notasi dengan b (mol)")
    parser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)
