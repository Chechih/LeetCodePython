from typing import List

class Solution:
    def buildMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        return matrix
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = self.buildMatrix(n)
        loop = 0
        right = len(matrix[0]) - 1
        left = top = 0
        bottom = len(matrix) - 1
        allNum = list(range(1, n * n + 1))
        allNumInd = 0

        while(right >= left and bottom >= top):
            ind = loop % 4 #在上下左右
            if(ind == 0):
                for i in range(left, right + 1):
                    matrix[top][i] = allNum[allNumInd]
                    allNumInd += 1
                top += 1
            elif(ind == 1):
                for i in range(top, bottom + 1):
                    matrix[i][right] = allNum[allNumInd]
                    allNumInd += 1
                right -= 1
            elif(ind == 2):
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = allNum[allNumInd]
                    allNumInd += 1
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = allNum[allNumInd]
                    allNumInd += 1
                left += 1
            loop += 1
        return matrix


tttt = Solution()
print(tttt.generateMatrix(3))   