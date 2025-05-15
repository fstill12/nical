from collections import deque
from typing import List, Union, Tuple


def rotate_left(arr: List[any], pivot: int) -> List[any]:
    """
    Rotasi ke kiri dengan posisi pivot.
    """
    arr = deque(arr)
    arr.rotate(-pivot)  # negatif berarti geser ke kiri
    return list(arr)

def gets_data_arr(arr: List[any], valeu: any) -> Union[int, List[any]]: 
    """
    Mengambil indeks array berdasarkan isinya.
    """
    if valeu in arr:
        return arr.index(valeu)
    else:
        return arr
    
def rotate_array(arr: List[any], valeu: any) -> List[any]:
    """
    Merotasi dan membuat array baru berdasarkan value.
    """
    data = gets_data_arr(arr=arr, valeu=valeu) 
    return rotate_left(arr=arr, pivot=data)

def achord(note_tuts: List[str], tuts: str, q: List[str]) -> Tuple[str]:
    """
    Membuat akor berdasarkan array q dan tuts
    """
    rotasi = rotate_array(arr=note_tuts, valeu=tuts)
    return [ rotasi[a] if a < len(rotasi) else rotasi[ a % len(rotasi) ]  for a in q]


# if __name__ == "__main__":
#     NOTE_NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F',
#                 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

#     data = gets_data_arr(NOTE_NAMES, 'A')
#     rotasi = rotate_left(NOTE_NAMES, data)
#     print(NOTE_NAMES)
#     print(data)
#     print(rotasi)
#     print()
#     print(rotate_array(NOTE_NAMES, 'D'))
#     print()
#     print(achord(note_tuts=NOTE_NAMES, tuts="C", q=[0, 4, 7, 10, 14]))