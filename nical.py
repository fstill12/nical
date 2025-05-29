import argparse
from teori import achord, Note
from teori.interval import mayor, minor, diminished, augmented, rumus_tangga_nada
import re
import sys
import contextlib
import io

# nical.py - Aplikasi pembuat akor musik

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
    """Cek apakah input tuts valid."""
    return bool(re.fullmatch(r"[A-Ga-g][#b]?", tuts))

def validate_tuts(tuts: str) -> str | None:
    """Validasi input tuts."""
    if tuts is None:
        return "Kesalahan: perintah --tuts belum diberikan."
    if not is_valid_str(tuts):
        return "Kesalahan: Input hanya boleh berupa huruf A–G diikuti opsional '#' atau 'b'."
    return None

def run_chord(args: argparse.Namespace):
    """Fungsi untuk menangani perintah 'chord'."""
    error = validate_tuts(args.tuts)
    if error:
        print(error)
        return

    kunci = convert_tuts_to_notasi(args.tuts, args.notasi)
    n = Note.sharp if args.notasi == "sharp" else Note.flat
    # validasi interval
    mapping = {
        "mayor": mayor,
        "minor": minor,
        "diminished": diminished,
        "augmented": augmented
    }

    mode = mapping[args.interval]
    print()
    print(f"Tangga nada {kunci} {mode.simbol['title']}".title())
    print()
    # tampilkan hasil
    for x, y in mode.simbol[args.interval].items():
        hasil = achord(note=n, tuts=kunci, q=y)
        if args.verbose:
            print()
            print(f"Tangga nada {kunci}")
            print(f"Interval {x.replace('C', kunci).title()}")
            print(f"Notasi {args.notasi.title()}")
            print(f"Akor {x.replace('C', kunci)} = {hasil}")
            print()
        else:
            print(hasil)

def run_scale(args: argparse.Namespace):
    """Fungsi untuk menangani perintah 'scale'."""
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
    # tampilkan hasil
    if args.verbose:
        print()
        print(f"Tangga nada {kunci}")
        print(f"Interval {map.title()}")
        print(f"Notasi {args.notasi.title()}")
        print(f"\nSkala  {kunci} {map.title()}:\n{' - '.join(rtn)}")
        if args.interval != "kromatik":
            print("\nNilai setiap nada dalam skala:")
            for i, note in enumerate(rtn):
                print(f"{i+1}. {note} ({Note.derajat[i+1]})")
    else:
        print(f"\nSkala  {kunci} {map.title()}:\n{' - '.join(rtn)}\n")
        print(f"{kunci} {map.title()} = {rtn}\n")

def run_placeholder(command_name: str):
    """Fungsi placeholder untuk perintah yang masih dalam pengembangan."""
    def _inner(_args):
        print(f"🔧 Fitur '{command_name}' masih dalam pengembangan. Nantikan update berikutnya!")
    return _inner

def main():
    """Fungsi utama untuk menjalankan aplikasi Nical."""
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
                              choices=["mayor", "mayor_pentatonik", "minor",
                                        "minor_harmonik", "minor_melodik", "minor_pentatonik",
                                        "blues", "whole_tone", "kromatik"],
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

    # help
    set_args_parse = {
        "chord -h --help": chord_parser, "scale -h --help": scale_parser, 
          "analyze -h --help": analyze_parser, "suggest -h --help": suggest_parser
        } # daftar perintah bantuan
    nc = sys.argv # ambil argumen dari command line
    if len(nc) == 1:
        parser.print_help()
        sys.exit()
    else:
        # tangani bantuan khusus subcammand
        for argp, comm in set_args_parse.items():
            if " ".join(nc[1:]) in argp:
                comm.print_help()
                sys.exit()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
