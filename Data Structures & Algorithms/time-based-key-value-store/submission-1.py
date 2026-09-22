class TimeMap:

    def __init__(self):
        self.d = {} # stores keys mapped to a list of (timestamp, value) tuples
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d: 
            self.d[key] = []
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: 
            return ""
        lst = self.d[key]
        l, r = 0, len(lst) - 1
        res = ""
        while l <= r: 
            mid = l + (r - l) // 2
            time = lst[mid][0]
            val = lst[mid][1]
            if timestamp == time: 
                return val
            elif timestamp > time: 
                res = val
                l = mid + 1
            else: 
                r = mid - 1
        return res

