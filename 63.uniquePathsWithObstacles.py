from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0] * n for i in range(m)]
        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                    continue
                if i - 1 >= 0 :
                    grid[i][j] += grid[i - 1][j]
                if j - 1 >= 0 :
                    grid[i][j] += grid[i][j - 1]
        return grid[m - 1][n - 1]

tttt = Solution()
print(tttt.uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,0,0]]))