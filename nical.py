import argparse
from teori import achord, rumus_tangga_nada, SplitDict, validate_tuts, convert_tuts_to_notasi, is_valid_akor
from teori.interval import mayor, minor, diminished, augmented
from teori.interval.note import Note, Diatonik
import sys

# MusikaCLI.py - Aplikasi pembuat akor musik

# run_chord - Fungsi untuk menangani perintah 'chord'
class RunChord:
    def __init__(self, args: dict[str, str]):
        self.args = args

    def validate_string(self):
        """Fungsi untuk validasi string"""
        error = validate_tuts(self.args.tuts)
        if error:
            print(error)
            return
        
    def coversi_notasi_tuts(self, kunci: str, notasi: str) -> str:
        """konversi notasi tuts tunggal ke flat atau sharp"""
        return convert_tuts_to_notasi(kunci, notasi)
    
    def buat_interval(self, interval: str) -> dict[str, str]:
        """ambil data interval"""
        mapping = {
            "mayor": mayor,
            "major": mayor,
            "minor": minor,
            "diminished": diminished,
            "augmented": augmented
        }
        return mapping[interval].simbol
    
    def judul(self, interval: str) -> str:
        """ambil data judul dari metode buat_interval"""
        return self.buat_interval(interval).get("title")
    
    def ambil_simbol(self, tuts: str) -> dict[str, str]:
        """membuat data tangga nada baru dan simbol sebagai nilai tuts sebegai kunci"""
        # ambil simbol dari interval
        mode = self.buat_interval(self.args.interval)
        vsimbol = SplitDict(mode[self.args.interval])
        # validasi simbol
        return {f"{tuts}{v[0]}": v[1] for v in Note.quality if v[1] in vsimbol.nilai()}
    
    def notasi(self, nn: str) -> list[str]:
        """mengembalikan notasi flat atau sharp berdasarkan nn"""
        return Note.sharp if nn == "sharp" else Note.flat
        
    def olah_data(self) -> dict:
        """membuat dan menyimpan notasi dan tangga baru"""
        judul = self.judul(self.args.interval)
        kunci = self.coversi_notasi_tuts(self.args.tuts, self.args.notasi)
        notasi = self.notasi(self.args.notasi)
        tangga_baru = self.ambil_simbol(kunci)
        return {"judul": judul, "kunci": kunci, "notasi": notasi, "tangga_nada": tangga_baru}
    
    def tampil_ke_terminal(self) -> None:
        """menampilkan data ke terminal"""
        data_baru = self.olah_data()
        print()
        print(f"Tangga nada {data_baru.get("kunci")} {data_baru.get("judul")}")
        print(f"Simbol : {data_baru.get("kunci")}{Note.stn[data_baru.get("judul")]}")
        print()
        # tampilkan hasil
        for x, y in data_baru.get("tangga_nada").items():
            hasil = achord(note=data_baru.get("notasi"), tuts=data_baru.get("kunci"), q=y)
            if self.args.verbose:
                print()
                print(f"Tangga nada : {data_baru.get("kunci")}")
                print(f"Interval : {x.title()}")
                print(f"Notasi : {self.args.notasi.title()}")
                print(f"Akor : {x} = {hasil}")
            else:
                print(f"Akor : {x} = {hasil}")
        print()

def run_chord(args: argparse.Namespace):
    """Fungsi untuk menangani perintah 'chord'."""
    rc = RunChord(args)
    rc.validate_string()
    rc.tampil_ke_terminal()

class RunScale:
    def __init__(self, args: dict[str, str]):
        self.args = args

    def validate_string(self):
        """Fungsi untuk validasi string"""
        error = validate_tuts(self.args.tuts)
        if error:
            print(error)
            return
        
    def coversi_notasi_tuts(self, kunci: str, notasi: str) -> str:
        """konversi notasi tuts tunggal ke flat atau sharp"""
        return convert_tuts_to_notasi(kunci, notasi)
    
    def tangga_nada_universal(self, kunci: str, interval: dict[str, str], notasi: str) -> str:
        """membuat skala dari akar kunci, interval dan notasi"""
        return rumus_tangga_nada.build_scale(root_name=kunci, intervals=interval, use=notasi)

    def tangga_major(self) -> dict[str, str]:
        """tangga nada major"""
        return SplitDict(Diatonik.mayor["tangga_nada"])
    
    def tangga_minor(self) -> dict[str, str]:
        """tangga nada minor"""
        return SplitDict(Diatonik.minor["tangga_nada"])
    
    def buat_interval(self, interval: str) -> dict[str, any]:
        """ambil data interval"""
        mapping = {
            "mayor": "mayor",
            "mayor_pentatonik": "mayor_pentatonik",
            "minor": "minor",
            "minor_harmonik": "minor_harmonik",
            "minor_melodik": "minor_melodik",
            "minor_pentatonik": "minor_pentatonik",
            "blues": "blues",
            "whole_tone": "whole_tone",
            "kromatik": "kromatik"
        }
        map = mapping[interval]
        return {"nama_interval": map, "interval": Note.tangga_nada["tangga_nada"][map]}
    
    def notasi(self, nn: str) -> list[str]:
        """mengembalikan notasi flat atau sharp berdasarkan nn"""
        return Note.sharp if nn == "sharp" else Note.flat
    
    def tampilkan_ke_terminal(self) -> None:
        """menampilkan data ke terminal"""
        kunci = self.coversi_notasi_tuts(self.args.tuts, self.args.notasi)
        interval = self.buat_interval(self.args.interval)
        notasi = self.notasi(self.args.notasi)
        rtn = self.tangga_nada_universal(kunci, interval.get("interval"), notasi)
        tminor = self.tangga_minor()
        tmayor = self.tangga_major()
        if self.args.verbose:
            print()
            print(f"Tangga nada : {kunci}")
            print(f"Simbol : {kunci}{Note.stn.get(interval.get("nama_interval"), '')}")
            print(f"Interval : {interval.get("interval")}")
            print(f"Notasi : {self.args.notasi}")
            print(f"\nSkala : {kunci} {interval.get("nama_interval").replace("_", " ")}:\n{' - '.join(rtn)}")
            print("\nNilai setiap nada dalam skala:")
            for i, note in enumerate(rtn):
                der = Note.derajat.get(i+1, f"{i+1}")
                print(f"{i+1}. {note} ({der})")
            # Diatonik hanya untuk mayor/minor
            if interval.get("nama_interval") == "mayor":
                print(f"\nTangga nada diatonik : {kunci}{Note.stn[interval.get("nama_interval")]}")
                tgmayor = [f"{rtn[t]}{Note.stn[s]}" for t, s in enumerate(tmayor.nilai())]
                for k, v in zip(tmayor.kunci(), tgmayor):
                    print(f"{k} : {v}")
                print()
            if interval.get("nama_interval") == "minor":
                print(f"\nTangga nada diatonik : {kunci}{Note.stn[interval.get("nama_interval")]}")
                tgminor = [f"{rtn[t]}{Note.stn[s]}" for t, s in enumerate(tminor.nilai())]
                for k, v in zip(tminor.kunci(), tgminor):
                    print(f"{k} : {v}")
                print()
        else:
            print(f"Simbol : {kunci}{Note.stn.get(interval.get("nama_interval"), '')}")
            print(f"\nSkala : {kunci} {interval.get("nama_interval").replace("_", " ")}:\n{' - '.join(rtn)}\n")
            print(f"{kunci} {interval.get("nama_interval")} = {rtn}\n")
            print("Nilai setiap nada dalam skala:")
            for i, note in enumerate(rtn):
                der = Note.derajat.get(i+1, f"{i+1}")
                print(f"{i+1}. {note} ({der})")
            # Diatonik hanya untuk mayor/minor
            if interval.get("nama_interval") == "mayor":
                print(f"\nTangga nada diatonik : {kunci}{Note.stn[interval.get("nama_interval")]}")
                tgmayor = [f"{rtn[t]}{Note.stn[s]}" for t, s in enumerate(tmayor.nilai())]
                for k, v in zip(tmayor.kunci(), tgmayor):
                    print(f"{k} : {v}")
                print()
            if interval.get("nama_interval") == "minor":
                print(f"\nTangga nada diatonik : {kunci}{Note.stn[interval.get("nama_interval")]}")
                tgminor = [f"{rtn[t]}{Note.stn[s]}" for t, s in enumerate(tminor.nilai())]
                for k, v in zip(tminor.kunci(), tgminor):
                    print(f"{k} : {v}")
                print()

# run_scale - Fungsi untuk menangani perintah 'scale' 
def run_scale(args: argparse.Namespace):
    """Fungsi untuk menangani perintah 'scale'."""
    rs = RunScale(args)
    rs.validate_string()
    rs.tampilkan_ke_terminal()

# run_analyze - Fungsi untuk menganal isis tuts/nada dan menebak jenis akor
def run_analyze(args: argparse.Namespace):
    """Fungsi untuk menganalisis tuts/nada dan menebak jenis akor."""
    tuts_list = is_valid_akor(args.tuts)
    for t in tuts_list:
        error = validate_tuts(t)
        if error:
            print(error)
            return

    kunci = convert_tuts_to_notasi(tuts_list[0], args.notasi)
    n = Note.sharp if args.notasi == "sharp" else Note.flat

    # Cek kecocokan dengan kualitas akor yang ada
    cocok = []
    for nama, interval in Note.quality:
        hasil = achord(note=n, tuts=kunci, q=interval)
        if set(hasil) == set(tuts_list):
            cocok.append(nama)

    print(f"\nAnalisis untuk tuts: {args.tuts}")
    if cocok:
        print("Kemungkinan akor:")
        for nama in cocok:
            print(f"- {kunci}{nama}")
    else:
        print("Tidak ditemukan akor yang cocok.")

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
