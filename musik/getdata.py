from dataclasses import dataclass
from teori.interval import mayor, minor, diminished, augmented
from utils.note import Note, Diatonik
from utils.split import SplitDict
import json

@dataclass
class DataKonstanta:
    """ambil data dari paket musik.utils.note atau musik.teori.interval"""
    __data: dict[str, str]

    @property
    def getDict(self) -> SplitDict:
        datas = SplitDict(self.__data)
        return datas
    
@dataclass
class Akor:
    """ambil konci dari semua data dari paket musik.teori.interval"""
    __tangga: str

    def __post_init__(self):
        if self.__tangga in ['major', 'mayor']:
            self.__nada = mayor.simbol.get('mayor')
        if self.__tangga == ['minor', 'min']:
            self.__nada = minor.simbol.get('minor')
        if self.__tangga == ['diminished', 'dim]']:
            self.__nada = diminished.simbol.get('diminished')
        if self.__tangga in ["augmented", "aug"]:
            self.__nada = augmented.simbol.get('augmented')

    @property
    def getData(self) -> list[str]:
        dd = DataKonstanta(self.__nada.simbol)
        return dd.get_data.kunci()
    
@dataclass
class JsonFile:
    """mengatur berkas json"""
    path: str

    def jsonfile(self, datafile: any):
        """membuat data json"""
        with open(self.path, "w") as f:
            json.dump(datafile, f, indent=4)

@dataclass
class getArray:
    """ambil array"""
    array: list
    
@dataclass
class Error:
    """atur kelasahan"""
    error: str

@dataclass
class NoteTangga:
    """interval tangga nada"""
    note = {
        'flat': Note.flat, 
        'sharp': Note.sharp, 
        'tangga': Note.tangga_nada, 
        'derajat': Note.derajat,
        'simbol': Note.stn, 
        'kualitis': Note.quality,
        'mayor': Diatonik.mayor,
        'minor': Diatonik.minor}

@dataclass
class Utilitis:
    """utilitis data"""
    util: str

    def __post_init__(self):
        note = NoteTangga.note
        semua = DataKonstanta(note)
        if self.util in semua.getDict.kunci():
            self.utilitas = note.get(self.util)
        else:
            self.__error = self.util

    def cekUtils(self) -> getArray | DataKonstanta:
        """perikas error parameter"""
        try:
            if isinstance(self.utilitas, list):
                return getArray(self.utilitas)
            if isinstance(self.utilitas, dict):
                return DataKonstanta(self.utilitas)
        except AttributeError:
            return Error(self.__error)
        
    def getNote(self) -> NoteTangga:
        return NoteTangga
    
    def setJson(self, path: str) -> JsonFile:
        return JsonFile(path=path)


if __name__=="__main__":
    tt = Utilitis('flat')
    alamat = "simpan/data.json"
    print(tt.cekUtils().array)
    print(tt.getNote().note)
    print(tt.setJson(alamat).jsonfile(tt.getNote().note))