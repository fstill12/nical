import argparse
from teori import achord, Note
from teori.interval import mayor, minor, diminished, augmented
import re
import sys

def is_valid_str(tuts: str) -> bool:
    return bool(re.fullmatch(r"[A-Ga-g][#b]?", tuts))

def validate_tuts(tuts: str) -> str | None:
    if tuts is None:
        return "Kesalahan: perintah --tuts belum diberikan."
    if not is_valid_str(tuts):
        return "Kesalahan: Input hanya boleh berupa huruf A–G diikuti opsional '#' atau 'b'."
    return None

def run_chord(args: argparse.Namespace):
    error = validate_tuts(args.tuts)
    if error:
        print(error)
        return

    kunci = args.tuts.title()
    n = Note.sharp if args.notasi == "sharp" else Note.flat

    mapping = {
        "mayor": mayor,
        "minor": minor,
        "diminished": diminished,
        "augmented": augmented
    }

    mode = mapping[args.interval]
    print()
    print(f"Tangga nada {mode.simbol['title']}".title())
    print()

    for x, y in mode.simbol[args.interval].items():
        hasil = achord(note=n, tuts=kunci, q=y)
        if args.verbose:
            print(f"Akor {x.replace('C', kunci)} = {hasil}")
        else:
            print(hasil)

def run_placeholder(command_name: str):
    def _inner(_args):
        print(f"🔧 Fitur '{command_name}' masih dalam pengembangan. Nantikan update berikutnya!")
    return _inner

def main():
    parser = argparse.ArgumentParser(prog="nical", description="🎵 Nical - Aplikasi pembuat akor musik")
    subparsers = parser.add_subparsers(title="perintah", dest="command", required=True)

    # chord
    chord_parser = subparsers.add_parser("chord", help="Buat akor berdasarkan tuts")
    chord_parser.add_argument("-t", "--tuts", required=True, help="Tuts dasar (misal: C, D#, Bb)")
    chord_parser.add_argument("-i", "--interval", required=True, choices=["mayor", "minor", "diminished", "augmented"], help="Jenis interval akor")
    chord_parser.add_argument("-n", "--notasi", required=True, choices=["sharp", "flat"], help="Jenis notasi (# atau b)")
    chord_parser.add_argument("-v", "--verbose", action="store_true", help="Tampilkan hasil lengkap")
    chord_parser.set_defaults(func=run_chord)

    # scale
    scale_parser = subparsers.add_parser("scale", help="(Dalam pengembangan) Buat tangga nada")
    scale_parser.set_defaults(func=run_placeholder("scale"))

    # analyze
    analyze_parser = subparsers.add_parser("analyze", help="(Dalam pengembangan) Analisa akor")
    analyze_parser.set_defaults(func=run_placeholder("analyze"))

    # suggest
    suggest_parser = subparsers.add_parser("suggest", help="(Dalam pengembangan) Rekomendasi progresi akor")
    suggest_parser.set_defaults(func=run_placeholder("suggest"))

    nc = sys.argv
    if len(nc) == 1:
        parser.print_help()
        sys.exit()
    else:
        # tangani bantuan khusus subcammand
        if " ".join(nc[1:]) in "chord -h --help":
            chord_parser.print_help()
            sys.exit()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
