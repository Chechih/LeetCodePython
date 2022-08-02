from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        newgrid = [[0] * n for i in range(m)]
        newgrid[0][0] = grid[0][0] 
        for i in range(m):
            for j in range(n):
                top = -1
                left = -1
                if i - 1 >= 0 :
                    top = newgrid[i - 1][j]
                if j - 1 >= 0 :
                    left = newgrid[i][j - 1]
                top = top if top != -1 else left
                left = left if left != -1 else top
                if top == left == -1:
                    top = left = 0
                newgrid[i][j] = grid[i][j] + min(top, left) 
        return newgrid[m - 1][n - 1]

tttt = Solution()
print(tttt.minPathSum(
[[0,2,2,6,4,1,6,2,9,9,5,8,4,4],[0,3,6,4,5,5,9,7,8,3,9,9,5,4],[6,9,0,7,2,2,5,6,3,1,0,4,2,5],[3,8,2,3,2,8,8,7,5,9,6,3,4,5],[4,0,1,3,9,2,0,1,6,7,9,2,8,9],[6,2,7,9,0,9,5,2,7,5,1,4,4,7],[9,8,3,3,0,6,8,0,8,8,3,5,7,3],[7,7,4,5,9,1,5,0,2,2,2,1,7,4],[5,1,3,4,1,6,0,4,3,8,4,3,9,9],[0,6,4,9,4,1,5,5,4,2,5,7,4,0],[0,1,6,6,4,9,2,7,8,2,1,3,3,7],[8,4,9,9,2,3,8,6,6,5,4,1,7,9]]))