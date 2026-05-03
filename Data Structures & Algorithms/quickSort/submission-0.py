# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def quickSortHelper(l, r, pairs):
            if r - l + 1 <= 1:
                return
            left = l
            for i in range(l, r):
                if pairs[i].key < pairs[r].key:
                    # swap them
                    temp = pairs[left]
                    pairs[left] = pairs[i]
                    pairs[i] = temp
                    left += 1
            # swap left and pivot
            temp = pairs[left]
            pairs[left] = pairs[r]
            pairs[r] = temp

            quickSortHelper(l, left - 1, pairs)
            quickSortHelper(left + 1, r, pairs)

        quickSortHelper(0, len(pairs) - 1, pairs)
        return pairs

            


        
