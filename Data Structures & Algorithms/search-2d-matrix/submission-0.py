class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        
        def binarySearch(l, r, row, target):

            if l > r:
                return False
            mid = (l + r) // 2
            if row[mid] == target:
                return True

            elif row[mid] > target:
                return binarySearch(l, mid - 1, row, target)
            else:
                return binarySearch(mid + 1, r, row, target)

        

        # check which row it is in:
        def matrixSearch(startRow, endRow, matrix, target):
            if startRow > endRow:
                return False

            midRow = (startRow + endRow) // 2
            if matrix[midRow][0] <= target <= matrix[midRow][len(matrix[midRow])-1]:
                return binarySearch(0, len(matrix[midRow]) - 1, matrix[midRow], target)

            elif matrix[midRow][0] > target:
                return matrixSearch(startRow, midRow - 1, matrix, target)
            else:
                return matrixSearch(midRow + 1, endRow, matrix, target)




        # now which line, then binary serach that line
        return matrixSearch(0, len(matrix) - 1, matrix, target)