from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return target in matrix[i - 1]
        return target in matrix[len(matrix) - 1]

tttt = Solution()
print(tttt.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))