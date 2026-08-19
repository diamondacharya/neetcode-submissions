class TimeMap:
    def __init__(self):
        self.keyStore = {} # stores key: list of (timestamp, value) tuples
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore: 
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ''        
        valList = self.keyStore.get(key, [])
        l, r = 0, len(valList) - 1
        while l <= r: 
            m = l + (r - l) // 2
            midTime, midVal = valList[m]
            if midTime > timestamp:                 
                r = m - 1
            else: 
                res = midVal
                l = m + 1
        return res
