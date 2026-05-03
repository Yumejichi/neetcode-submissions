class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = {}

        # for num in nums:
        #     if num in counts:
        #         counts[num] += 1
        #     else:
        #         counts[num] = 1

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
        # heap = []
        # for num in counts.keys():
        #     heapq.heappush(heap, (counts[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for i in range(len(heap)):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        # O(n) solution:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # make a list store the occurence frequency with the corresponding numbers
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in count.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for elem in freq[i]:
                res.append(elem)
                if len(res) == k:
                    return res
            

