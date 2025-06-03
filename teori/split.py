Intervals = dict[str, str]

class SplitDict:
    def __init__(self, interval: Intervals):
        self.interval = interval

    def kunci(self):
        return list(self.interval.keys())
    
    def nilai(self):
        return list(self.interval.values())
