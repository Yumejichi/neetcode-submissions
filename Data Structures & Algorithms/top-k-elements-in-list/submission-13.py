class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use an array to store the num under the index of occurence:
        frequency = [[] for _ in range(len(nums) + 1)]


        counts = Counter(nums)

        for num, count in counts.items():
            frequency[count].append(num)
        
        res = []
        for arr in reversed(frequency):
            if arr != []:
                for num in arr:
                    res.append(num)
                    k -= 1


                    if k == 0:
                        return res

