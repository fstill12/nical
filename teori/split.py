Intervals = dict[str, str]

class SplitDict:
    def __init__(self, interval: Intervals):
        self.interval = interval

    @property
    def keys(self):
        return list(self.interval.keys())
    
    @property
    def values(self):
        return list(self.interval.values())
