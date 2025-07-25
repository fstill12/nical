from teori import achord, rumus_tangga_nada, SplitDict, validate_tuts, convert_tuts_to_notasi, is_valid_akor
from teori.interval import mayor, minor, diminished, augmented
from teori.interval.note import Note, Diatonik
import sys

# MusikaCLI.py - Aplikasi pembuat akor musik

# run_chord - Fungsi untuk menangani perintah 'chord'
class RunChord:
    def __init__(self, args: argparse.Namespace):
        self.args = args

    def validate_string(self):
        """Fungsi untuk menangani perintah 'chord'."""
        error = validate_tuts(self.args.tuts)
        if error:
            print(error)
            return
        
    def coversi_notasi_tuts(self) -> str:
        """konversi notasi tuts tunggal ke flat atau sharp"""
        return convert_tuts_to_notasi(self.args.tuts, self.args.notasi)
    
    def buat_interval(self) -> dict[str, str]:
        """ambil data interval"""
        mapping = {
            "mayor": mayor,
            "major": mayor,
            "minor": minor,
            "diminished": diminished,
            "augmented": augmented
        }
        return mapping[self.args.interval].simbol
    
    def judul(self):
        """ambil data judul dari metode buat_interval"""
        return self.buat_interval().get("title")
    
    def ambil_simbol(self, tuts: str) -> dict[str, str]:
        """membuat data tangga nada baru dan simbol sebagai nilai tuts sebegai kunci"""
        # ambil simbol dari interval
        mode = self.buat_interval()
        vsimbol = SplitDict(mode[self.args.interval])
        # validasi simbol
        return {f"{tuts}{v[0]}": v[1] for v in Note.quality if v[1] in vsimbol.nilai()}
        
    def olah_data(self) -> dict:
        """membuat dan menyimpan notasi dan tangga baru"""
        kunci = self.coversi_notasi_tuts()
        notasi = Note.sharp if self.args.notasi == "sharp" else Note.flat
        tangga_baru = self.ambil_simbol(kunci)
        return {"kunci": kunci, "notasi": notasi, "tangga_nada": tangga_baru}
    
    def tampil_ke_terminal(self) -> None:
        data_baru = self.olah_data()
        print()
        print(f"Tangga nada {data_baru.get("kunci")} {self.judul()}")
        print(f"Simbol : {data_baru.get("kunci")}{Note.stn[self.judul()]}")
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