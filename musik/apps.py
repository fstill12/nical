from teori.achord import achord
from teori.interval import mayor, minor, diminished, augmented
from utils.note import Note, Diatonik
from utils import rumus_tangga_nada
from utils.split import SplitDict
from utils.validate import convert_tuts_to_notasi, is_valid_akor, is_valid_str
from typing import Union
from dataclasses import dataclass
import json

# MusikaCLI.py - Aplikasi pembuat akor musik

type Flat = str
type Sharp = str
type Huruf = str
type Angka = str


@dataclass
class Tangga:
    __nada: dict[str, str]

    def __post_init__(self):
        self.data = SplitDict(self.__nada)

    @property    
    def nada(self):
        return self.data

@dataclass
class Utils:
    args: dict[str, str]

    def validate_string(self) -> bool:
        """Fungsi untuk validasi string"""
        return is_valid_str(self.args.get("tuts", ""))
    
    def notasi(self, nn: str) -> list[str]:
        """mengembalikan notasi flat atau sharp berdasarkan nn"""
        return Note.sharp if nn == "sharp" else Note.flat

@dataclass
class RunChord(Utils):
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
        mode = self.buat_interval(self.args["interval"])
        vsimbol = SplitDict(mode[self.args["interval"]])
        # validasi simbol
        return {f"{tuts}{v[0]}": v[1] for v in Note.quality if v[1] in vsimbol.nilai()}
    
    def olah_data(self) -> dict:
        """membuat dan menyimpan notasi dan tangga baru"""
        judul = self.judul(self.args["interval"])
        kunci = self.coversi_notasi_tuts(self.args["tuts"], self.args["notasi"])
        notasi = self.notasi(self.args["notasi"])
        tangga_baru = self.ambil_simbol(kunci)
        return {"judul": judul, "kunci": kunci, "notasi": notasi, "tangga_nada": tangga_baru}
    
    def tampilkan_ke_terminal(self) -> None:
        """menampilkan data ke terminal"""
        data_baru = self.olah_data()
        print(f"\nTangga nada {data_baru['kunci']} {data_baru['judul']}")
        print(f"Simbol : {data_baru['kunci']}{Note.stn[data_baru['judul']]}\n")
        # tampilkan hasil
        for x, y in data_baru["tangga_nada"].items():
            hasil = achord(note=data_baru["notasi"], tuts=data_baru["kunci"], q=y)
            if self.args.get("verbose", False):
                print(f"\nTangga nada : {data_baru['kunci']}")
                print(f"Interval : {x.title()}")
                print(f"Notasi : {self.args['notasi'].title()}")
                print(f"Akor : {x} = {hasil}")
            else:
                print(f"Akor : {x} = {hasil}")
        print()

    def set_json(self) -> None:
        """membuat data json"""
        data_baru = self.olah_data()
        with open("simpan/hasi.json", "w") as f:
            json.dump(data_baru, f, indent=4)

@dataclass
class RunScale(Utils):
    def coversi_notasi_tuts(self, kunci: str, notasi: str) -> str:
        """konversi notasi tuts tunggal ke flat atau sharp"""
        return convert_tuts_to_notasi(kunci, notasi)

    def tangga_nada_universal(self, kunci: str, interval: dict[str, str], notasi: str) -> list[str]:
        """membuat skala dari akar kunci, interval dan notasi"""
        return rumus_tangga_nada.build_scale(root_name=kunci, intervals=interval, use=notasi)

    def tangga_major(self) -> SplitDict:
        """tangga nada major"""
        return SplitDict(Diatonik.mayor["tangga_nada"])

    def tangga_minor(self) -> SplitDict:
        """tangga nada minor"""
        return SplitDict(Diatonik.minor["tangga_nada"])
    
    def jenis_interval(self) -> tuple:
        """menyimpan jenis interval ke dalam tuple"""
        return (
            'mayor', 'mayor_pentatonik', 'minor',
            'minor_harmonik', 'minor_melodik', 'minor_pentatonik',
            'blues', 'whole_tone', 'kromatik'
        )

    def buat_interval(self, interval: str) -> dict[str, any]:
        """ambil data interval"""
        jenis_interval = self.jenis_interval()
        mapping = dict(zip(jenis_interval, jenis_interval))
        map = mapping[interval]
        return {"nama_interval": map, "interval": Note.tangga_nada["tangga_nada"][map]}

    def set_json(self, kunci: Huruf, notasi: Union[Flat, Sharp], tangga: Angka) -> None:
        """membuat file json tangga nada berdasarkan argumennya"""
        angka_kunci = [i+1 for i in range(9)]
        jenis_interval = self.jenis_interval()
        mapping = dict(zip(angka_kunci, jenis_interval))
        kunci = self.coversi_notasi_tuts(kunci, notasi)
        if tangga in mapping:
            interval = self.buat_interval(mapping[tangga])
        else:
            interval = self.buat_interval(jenis_interval[0])
        notasi = self.notasi(notasi)
        rtn = self.tangga_nada_universal(kunci, interval["interval"], notasi)
        # membuat file json
        with open("simpan/data.json", "w") as f:
            json.dump(rtn, f, indent=4)

    def tampilkan_ke_terminal(self) -> None:
        """menampilkan data ke terminal"""
        kunci = self.coversi_notasi_tuts(self.args["tuts"], self.args["notasi"])
        interval = self.buat_interval(self.args["interval"])
        notasi = self.notasi(self.args["notasi"])
        rtn = self.tangga_nada_universal(kunci, interval["interval"], notasi)
        tminor = self.tangga_minor()
        tmayor = self.tangga_major()
        print(f"\nTangga nada : {kunci}")
        print(f"Simbol : {kunci}{Note.stn.get(interval['nama_interval'], '')}")
        print(f"Interval : {interval['interval']}")
        print(f"Notasi : {self.args['notasi']}")
        print(f"\nSkala : {kunci} {interval['nama_interval'].replace('_', ' ')}:\n{' - '.join(rtn)}")
        print("\nNilai setiap nada dalam skala:")
        for i, note in enumerate(rtn):
            der = Note.derajat.get(i+1, f"{i+1}")
            print(f"{i+1}. {note} ({der})")
        # Diatonik hanya untuk mayor/minor
        if interval["nama_interval"] == "mayor":
            print(f"\nTangga nada diatonik : {kunci}{Note.stn[interval['nama_interval']]}")
            tgmayor = [f"{rtn[t]}{Note.stn[s]}" for t, s in enumerate(tmayor.nilai())]
            for k, v in zip(tmayor.kunci(), tgmayor):
                print(f"{k} : {v}")
            print()
        if interval["nama_interval"] == "minor":
            print(f"\nTangga nada diatonik : {kunci}{Note.stn[interval['nama_interval']]}")
            tgminor = [f"{rtn[t]}{Note.stn[s]}" for t, s in enumerate(tminor.nilai())]
            for k, v in zip(tminor.kunci(), tgminor):
                print(f"{k} : {v}")
            print()

@dataclass
class RunAnalyze(Utils):
    """kelas untuk menganalisis tuts/nada dan menebak jenis akor"""
    def validate_string(self) -> bool:
        """Fungsi untuk validasi string"""
        return is_valid_akor(self.args.get("tuts", ""))
    
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
        akor_valid = self.cek_akor(self.args["tuts"])
        kunci = convert_tuts_to_notasi(akor_valid[0], self.args["notasi"])
        n = self.notasi(self.args["notasi"])
        # Cek kecocokan dengan kualitas akor yang ada
        cocok = self.cek_kecocokan(kunci=kunci, notasi=n, akor=akor_valid)
        print(f"\nAnalisis untuk tuts: {self.args['tuts']}")
        if cocok:
            print("Kemungkinan akor:")
            for nama in cocok:
                print(f"- {kunci}{nama}")
        else:
            print("Tidak ditemukan akor yang cocok.")

@dataclass
class RunSuggest(Utils):
    """Rekomendasi progresi akor berdasarkan tuts dan notasi."""

    def rekomendasi_progresi(self, tipe: str = "mayor") -> list[list[str]]:
        # Progresi umum mayor dan minor (rujukan: Hooktheory, MusicTheory.net, dsb)
        progresi_mayor = [
            ["I", "IV", "V", "I"],      # klasik
            ["I", "vi", "IV", "V"],     # pop
            ["ii", "V", "I"],           # jazz turnaround
            ["I", "V", "vi", "IV"],     # axis progression
        ]
        progresi_minor = [
            ["i", "iv", "V", "i"],      # klasik minor
            ["i", "VI", "III", "VII"],  # pop minor
            ["ii°", "V", "i"],          # jazz minor
        ]
        return progresi_mayor if tipe == "mayor" else progresi_minor

    def tampilkan_ke_terminal(self):
        tuts = self.args.get("tuts", "C")
        notasi = self.args.get("notasi", "sharp")
        tipe = self.args.get("tipe", "mayor")
        kunci = convert_tuts_to_notasi(tuts, notasi)
        progresi_list = self.rekomendasi_progresi(tipe)
        print(f"\nRekomendasi progresi akor untuk {kunci} {tipe}:")
        for idx, progresi in enumerate(progresi_list, 1):
            akor = []
            for derajat in progresi:
                if tipe == "mayor":
                    simbol = Diatonik.mayor["tangga_nada"].get(derajat, "")
                else:
                    simbol = Diatonik.minor["tangga_nada"].get(derajat, "")
                akor.append(f"{kunci}{Note.stn.get(simbol, '')}{simbol if simbol else ''}")
            print(f"Progresi {idx}: {' - '.join(akor)}")
        print()