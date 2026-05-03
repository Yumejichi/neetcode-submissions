class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # sorted_values = sorted(counts.items(), key = lambda x: x[1], reverse = True)
        # print(sorted_values)
        # res = []

        # for item in sorted_values:
        #     if k <= 0:
        #         break
        #     res.append(item[0])
        #     k -= 1
        # return res

        # Use heap also klogn
        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res
            

