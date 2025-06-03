Intervals = dict[str, str]

class SplitDict:
    """
    Kelas ini digunakan untuk mengelola interval sebagai dictionary."""
    def __init__(self, interval: Intervals):
        self.interval = interval

    def kunci(self):
        """Mengembalikan daftar kunci dari interval."""
        return list(self.interval.keys())
    
    def nilai(self):
        """Mengembalikan daftar nilai dari interval."""
        return list(self.interval.values())
    
    def __getitem__(self, key: str) -> str:
        """Mengembalikan nilai dari interval berdasarkan kunci."""
        return self.interval[key]

class DictFactory:
    """Kelas ini digunakan untuk membuat SplitDict dari interval yang diberikan."""
    @staticmethod
    def buat(interval: Intervals) -> SplitDict:
        """Membuat SplitDict dari interval yang diberikan."""
        return SplitDict(interval)

    @staticmethod
    def dari_list(intervals: list[tuple[str, str]]) -> SplitDict:
        """Membuat SplitDict dari list tuple yang berisi interval."""
        interval_dict = {k: v for k, v in intervals}
        return DictFactory.buat(interval_dict)
    
