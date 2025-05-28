import argparse
from teori import achord, Note
from teori.interval import mayor, minor, diminished, augmented, rumus_tangga_nada
import re
import sys

# universal
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

    kunci = convert_tuts_to_notasi(args.tuts, args.notasi)
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
            print()

def run_scale(args: argparse.Namespace):
    error = validate_tuts(args.tuts)
    if error:
        print(error)
        return
    
    kunci = convert_tuts_to_notasi(args.tuts, args.notasi)
    n = Note.sharp if args.notasi == "sharp" else Note.flat

    mapping = {
        "mayor": "mayor",
        "minor": "minor",
        "minor_natural": "minor",
        "minor_harmonik": "minor_harmonik",
        "minor_melodik": "minor_melodik",
        "kromatik": "kromatik"
    }
    map = mapping[args.interval]
    interval = Note.tangga_nada["tangga_nada"][map]
    rtn = rumus_tangga_nada.build_scale(root_name=kunci, intervals=interval, use=n)
    # permasalahan baru = scale -t c# -i mayor -n flat
    if args.verbose:
        print()
        print(f"Tangga nada {kunci}")
    print()
    print(f"{kunci} {map.title()} = {rtn}")
    print()

def run_placeholder(command_name: str):
    def _inner(_args):
        print(f"🔧 Fitur '{command_name}' masih dalam pengembangan. Nantikan update berikutnya!")
    return _inner

def main():
    parser = argparse.ArgumentParser(prog="nical", 
                                     description="🎵 Nical - Aplikasi pembuat akor musik",
                                     formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(title="perintah", dest="command", required=True)

    # chord
    chord_parser = subparsers.add_parser("chord", help="Buat akor berdasarkan tuts")
    chord_parser.add_argument("-t", "--tuts", required=True, help="Tuts dasar (misal: C, D#, Bb)")
    chord_parser.add_argument("-i", "--interval", choices=["mayor", "minor", "diminished", "augmented"], help="Jenis interval akor")
    chord_parser.add_argument("-n", "--notasi", choices=["sharp", "flat"], help="Jenis notasi (# atau b)")
    chord_parser.add_argument("-v", "--verbose", action="store_true", help="Tampilkan hasil lengkap")
    chord_parser.set_defaults(func=run_chord)

    # scale
    scale_parser = subparsers.add_parser("scale", help="(Dalam pengembangan) Buat tangga nada")
    scale_parser.add_argument("-t", "--tuts", help="Tuts dasar (misal: C, D#, Bb)")
    scale_parser.add_argument("-i", "--interval", 
                              choices=["mayor", "minor", "minor_natural", 
                                                      "minor_harmonik", "minor_melodik", "kromatik"], 
                              help="Jenis interval akor")
    scale_parser.add_argument("-n", "--notasi", choices=["sharp", "flat"], help="Jenis notasi (# atau b)")
    scale_parser.add_argument("-v", "--verbose", action="store_true", help="Tampilkan hasil lengkap")
    scale_parser.set_defaults(func=run_scale)

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
        if " ".join(nc[1:]) in "scale -h --help":
            scale_parser.print_help()
            sys.exit()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
