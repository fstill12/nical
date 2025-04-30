from itertools import combinations
from typing import List

type Skala = List[str]


def kombinasi_skala(skala: Skala, n: int) -> Skala:
    return list(combinations(skala, n))

if __name__ == "__main__":
    skala_d_mayor = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
    ss = kombinasi_skala(skala_d_mayor, 4)
    for i, v in enumerate(ss):
        print(i + 1, v)