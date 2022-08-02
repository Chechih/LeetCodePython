from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        loop = 0
        rlt = []
        right = len(matrix[0]) - 1
        left = top = 0
        bottom = len(matrix) - 1

        while(right >= left and bottom >= top):
            ind = loop % 4 #在上下左右
            if(ind == 0):
                for i in range(left, right + 1):
                    rlt.append(matrix[top][i])
                top += 1
            elif(ind == 1):
                for i in range(top, bottom + 1):
                    rlt.append(matrix[i][right])
                right -= 1
            elif(ind == 2):
                for i in range(right, left - 1, -1):
                    rlt.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    rlt.append(matrix[i][left])
                left += 1
            loop += 1

        return rlt

tttt = Solution()
# print(tttt.spiralOrder([[6],[9],[7]]))
print(tttt.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(tttt.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# print(tttt.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13]]))

# print(tttt.spiralOrder([[1,2],[3,4]]))



# print(tttt.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))