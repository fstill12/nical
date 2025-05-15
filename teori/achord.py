from collections import deque
from typing import List, Any, Tuple, Union

def rotate_left(arr: List[Any], pivot: int) -> List[Any]:
    """
    Rotasi ke kiri dengan posisi pivot.
    """
    arr = deque(arr)
    arr.rotate(-pivot)  # negatif berarti geser ke kiri
    return list(arr)

def gets_data_arr(arr: List[Any], valeu: Any) -> Union[Tuple[Any], int]: 
    """
    Mengambil data dari arr berdasarkan value.
    """
    for i, v in enumerate(arr):
        if valeu == v:
            return i, v
    else:
        return -1

# if __name__ == "__main__":
#     NOTE_NAMES = ['C', 'C_Sharp', 'D', 'D_Sharp', 'E', 'F',
#                 'F_Sharp', 'G', 'G_Sharp', 'A', 'A_Sharp', 'B']

#     data = gets_data_arr(NOTE_NAMES, 'A')
#     rotasi = rotate_left(NOTE_NAMES, data[0])
#     print(NOTE_NAMES)
#     print(data)
#     print(rotasi)