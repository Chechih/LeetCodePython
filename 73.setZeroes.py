from typing import List
from typing import Tuple
from typing import Set

class Solution:
    def findZeros(self, matrix: List[List[int]]) -> Set[Tuple[int, int]]:
        rlt = []
        leg = len(matrix)
        for i in range(leg):
            mm = matrix[i]
            rlt += [(i, j) for j in range(len(mm)) if mm[j] == 0]
        return set(rlt)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = self.findZeros(matrix)
        n = len(matrix)
        m = len(matrix[0])
        for zi, zj in zeros:
            for i in range(n):
                matrix[i][zj] = 0
            for j in range(m):
                matrix[zi][j] = 0
        return

tttt = Solution()
print(tttt.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
