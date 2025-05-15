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

if __name__ == "__main__":
    # nama-nama tuts
    NOTE_NAMES = ['C', 'C_Sharp', 'D', 'D_Sharp', 'E', 'F',
                'F_Sharp', 'G', 'G_Sharp', 'A', 'A_Sharp', 'B']

    arr = [1, 2, 3, 4]
    print(arr.index(1))
    print(gets_data_arr(NOTE_NAMES, 'r'))
    print(rotate_left(arr, 1))