class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hmap[key]
        left, right = 0, len(values)-1

        result = ""
        while left <= right:
            mid = left + (right-left) // 2
            val, time = values[mid]
            # Comparing times, update left or right accordingly
            if time <= timestamp:
                result = val
                left = mid + 1
            else:
                right = mid - 1
        return result
        
