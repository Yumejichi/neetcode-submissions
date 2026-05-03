class TimeMap:

    def __init__(self):
        self.personsDetail = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.personsDetail[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        print(self.personsDetail)
        if key in self.personsDetail:
            arr = self.personsDetail[key]
            print(arr)
            print(arr[-1][0])
            # # use binary search to get the closest timestamp
            l, r = 0, len(arr)-1
            closest = -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][1] <= timestamp:
                    closest = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return arr[closest][0] if closest != -1 else ""
        else:
            return ""