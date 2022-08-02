from typing import List
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = np.array(matrix)
        mat90 = list(np.rot90(mat, -1))
        matrix[:] = [list(m) for m in mat90]

tttt = Solution()
aaa = [[1,2,3],[4,5,6],[7,8,9]]
tttt.rotate(aaa)