class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        data = self.store[key]
        l,r = 0,len(data)-1
        ans = -1
        while l <= r:
            m = (l + r)//2
            if data[m][0] > timestamp:
                r = m - 1
            else:
                ans = m
                l = m + 1
        return data[ans][1] if ans != -1 else ""
        
