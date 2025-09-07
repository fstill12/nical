from teori import achord, rumus_tangga_nada, SplitDict, validate_tuts, convert_tuts_to_notasi, is_valid_akor
from teori.interval import mayor, minor, diminished, augmented
from teori.interval.note import Note, Diatonik
from typing import Union
import json

# MusikaCLI.py - Aplikasi pembuat akor musik

type Flat = str
type Sharp = str
type Huruf = str
type Angka = str

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

    def set_json(self) -> None:
        """membuat data json"""
        data_baru = self.olah_data()
        with open("simpan/hasi.json", "w") as f:
            json.dump(data_baru, f, indent=4)

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
    
    def jenis_interval(self) -> tuple:
        """menyimpan jenis interval ke dalam tuple"""
        return ['mayor', 'mayor_pentatonik', 'minor', 
                          'minor_harmonik', 'minor_melodik', 'minor_pentatonik', 
                          'blues', 'whole_tone', 'kromatik']
    
    def buat_interval(self, interval: str) -> dict[str, any]:
        """ambil data interval"""
        jenis_interval = self.jenis_interval()
        mapping = dict(zip(jenis_interval, jenis_interval))
        map = mapping[interval]
        return {"nama_interval": map, "interval": Note.tangga_nada["tangga_nada"][map]}
    
    def notasi(self, nn: str) -> list[str]:
        """mengembalikan notasi flat atau sharp berdasarkan nn"""
        return Note.sharp if nn == "sharp" else Note.flat
    
    def set_json(self, kunci: Huruf, notasi: Union[Flat, Sharp], tangga: Angka) -> None:
        """membuat file json tangga nada berdasarkan argumennya"""
        angka_kunci = [i+1 for i in range(9)]
        jenis_interval = self.jenis_interval()
        mapping = dict(zip(angka_kunci, jenis_interval))
        kunci = self.coversi_notasi_tuts(kunci, notasi)
        if tangga in list(mapping.keys()):
            interval = self.buat_interval(mapping.get(tangga))
        notasi = self.notasi(notasi)
        rtn = self.tangga_nada_universal(kunci, interval.get("interval"), notasi)
        # membuat file json
        with open("simpan/data.json", "w") as f:
            json.dump(rtn, f, indent=4)
    
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


class RunAnalyze:
    """kelas untuk menganalisis tuts/nada dan menebak jenis akor"""
    def __init__(self, args: dict[str, str]):
        self.args = args

    def validate_string(self):
        """Fungsi untuk validasi string"""
        akor_valid = self.cek_akor(self.args.tuts)
        for t in akor_valid:
            error = validate_tuts(t)
            if error:
                print(error)
                return
        
    def notasi(self, nn: str) -> list[str]:
        """mengembalikan notasi flat atau sharp berdasarkan nn"""
        return Note.sharp if nn == "sharp" else Note.flat
    
    def cek_akor(self, kunci: Huruf):
        """cek input adalah akor"""
        return is_valid_akor(kunci)
    
    def cek_kecocokan(self, kunci: Huruf, notasi: Union[Flat, Sharp], akor: list) -> list:
        """Cek kecocokan dengan kualitas akor yang ada"""
        cocok = []
        for nama, interval in Note.quality:
            hasil = achord(note=notasi, tuts=kunci, q=interval)
            if set(hasil) == set(akor):
                cocok.append(nama)
        return cocok

    def tampilkan_ke_terminal(self):
        """menampilkan ke layar"""
        akor_valid = self.cek_akor(self.args.tuts)
        kunci = convert_tuts_to_notasi(akor_valid[0], self.args.notasi)
        n = self.notasi(self.args.notasi)
        # Cek kecocokan dengan kualitas akor yang ada
        cocok = self.cek_kecocokan(kunci=kunci, notasi=n, akor=akor_valid)
        print(f"\nAnalisis untuk tuts: {self.args.tuts}")
        if cocok:
            print("Kemungkinan akor:")
            for nama in cocok:
                print(f"- {kunci}{nama}")
        else:
            print("Tidak ditemukan akor yang cocok.")