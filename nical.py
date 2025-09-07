import argparse
from apps import RunChord, RunScale, RunAnalyze, RunSuggest
import sys

# MusikaCLI.py - Aplikasi pembuat akor musik

def run_chord(args: argparse.Namespace):
    """Fungsi untuk menangani perintah 'chord'."""
    rc = RunChord(vars(args))  # konversi Namespace ke dict
    valid = rc.validate_string()
    if not valid:
        print("Kesalahan: Input hanya boleh berupa huruf A–G diikuti opsional '#' atau 'b'.")
    else:
        rc.tampil_ke_terminal()

# run_scale - Fungsi untuk menangani perintah 'scale' 
def run_scale(args: argparse.Namespace):
    """Fungsi untuk menangani perintah 'scale'."""
    rs = RunScale(vars(args))
    valid = rs.validate_string()
    if not valid:
        print("Kesalahan: Input hanya boleh berupa huruf A–G diikuti opsional '#' atau 'b'.")
    else:
        rs.tampilkan_ke_terminal()

# run_analyze - Fungsi untuk menganal isis tuts/nada dan menebak jenis akor
def run_analyze(args: argparse.Namespace):
    """Fungsi untuk menganalisis tuts/nada dan menebak jenis akor."""
    ra = RunAnalyze(vars(args))
    valid = ra.validate_string()
    if not valid:
       print("Kesalahan: Input hanya boleh berupa huruf A–G diikuti opsional '#' atau 'b'.")
    else: 
        ra.tampilkan_ke_terminal()

def run_suggest(args: argparse.Namespace):
    """Fungsi untuk memberikan saran progresi akor."""
    rs = RunSuggest(vars(args))
    rs.tampilkan_ke_terminal()

# run_placeholder - Fungsi placeholder untuk perintah yang masih dalam pengembangan
def run_placeholder(command_name: str):
    """Fungsi placeholder untuk perintah yang masih dalam pengembangan."""
    def _inner(_args):
        print(f"🔧 Fitur '{command_name}' masih dalam pengembangan. Nantikan update berikutnya!")
    return _inner

def main():
    """Fungsi utama untuk menjalankan aplikasi MusikaCLI."""
    parser = argparse.ArgumentParser(prog="MusikaCLI", 
                                     description="🎵 MusikaCLI - Aplikasi pembuat akor musik",
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
    scale_parser = subparsers.add_parser("scale", help="Buat tangga nada")
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
    analyze_parser = subparsers.add_parser("analyze", help="Analisa akor dari tuts")
    analyze_parser.add_argument("-t", "--tuts", required=True, help="Tuts/nada yang akan dianalisis (misal: C E G)")
    analyze_parser.add_argument("-n", "--notasi", choices=["sharp", "flat"], default="sharp", help="Jenis notasi (# atau b)")
    analyze_parser.set_defaults(func=run_analyze)

    # suggest
    suggest_parser = subparsers.add_parser("suggest", help="Rekomendasi progresi akor")
    suggest_parser.add_argument("-t", "--tuts", help="Tuts dasar (misal: C, D#, Bb)")
    suggest_parser.add_argument("-n", "--notasi", choices=["sharp", "flat"], default="sharp", help="Jenis notasi (# atau b)")
    suggest_parser.add_argument("--tipe", choices=["mayor", "minor"], default="mayor", help="Jenis progresi akor")
    suggest_parser.set_defaults(func=run_suggest)

    # help
    set_args_parse = {
        "chord -h --help": chord_parser, "scale -h --help": scale_parser, 
          "analyze -h --help": analyze_parser, "suggest -h --help": suggest_parser
        } # daftar perintah bantuan
    nc = sys.argv
    if len(nc) == 1:
        print("Silakan masukkan perintah. Gunakan -h untuk bantuan.")
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
