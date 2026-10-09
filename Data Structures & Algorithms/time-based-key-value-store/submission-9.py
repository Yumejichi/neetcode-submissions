class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list) #key: [(time, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # use binary search to find the last timestamp smaeer or equal to the timestamp
        # find the last true in arr
        l, r = 0, len(self.timestamps[key])-1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            time, val = self.timestamps[key][mid]
            if time == timestamp:
                return val
            elif time < timestamp:
                res = val
                l = mid + 1
            else:
                r = mid - 1

        return res
        

        
