class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we first check which row we are gonna search with binary search
        # -> when the row[0] <= target <= row[last_index] -> this is the row we want to search
        # Then we do binary search on that row

        n, m = len(matrix), len(matrix[0])
        top, bottom = 0, n-1
        while top <= bottom:
            middle = (top+bottom)//2

            if matrix[middle][0] <= target <= matrix[middle][m-1]:
                # binary seach the target here
                l, r = 0, m-1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[middle][mid] == target:
                        return True
                    elif matrix[middle][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            
            elif matrix[middle][m-1] < target:
                top = middle + 1
            # elif matrix[middle][0] > target:
            else:
                bottom = middle - 1
            # else:
            #     return False
        return False



        