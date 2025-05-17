from collections import deque
from typing import List, Union

type Skala = List[str]
type SkalaBaru = List[str]
type isiSkala = str
type NomorTuts = List[int]
type Tuts = str


def rotate_left(arr: Skala, pivot: int) -> SkalaBaru:
    """
    Rotasi skala ke kiri dengan posisi pivot.
    """
    arr = deque(arr)
    arr.rotate(-pivot)  # negatif berarti geser ke kiri
    return list(arr)

def gets_data_arr(arr: Skala, valeu: isiSkala) -> Union[int, isiSkala]: 
    """
    Mengambil indeks skala berdasarkan isinya.
    """
    if valeu in arr:
        return arr.index(valeu)
    else:
        return -1
    
def rotate_array(arr: Skala, valeu: isiSkala) -> SkalaBaru:
    """
    Merotasi dan membuat skala baru berdasarkan nilainya.
    """
    data = gets_data_arr(arr=arr, valeu=valeu) 
    return rotate_left(arr=arr, pivot=data)

def achord(note: Skala, tuts: Tuts, q: NomorTuts) -> SkalaBaru:
    """
    Membuat akor berdasarkan nomor tuts dan tuts
    """
    rotasi = rotate_array(arr=note, valeu=tuts)
    return [ rotasi[a] if a < len(rotasi) else rotasi[ a % len(rotasi) ]  for a in q]