from typing import List

class Solution:
    def checkHorizontal(self, x: int, y: int, queens: List[tuple]) -> bool:
        '''
        檢查水平
        '''
        for qx, qy in queens:
            if qx == x and (qx, qy) != (x, y):
                return False
        return True
    def checkVertical(self, x: int, y: int, queens: List[tuple]) -> bool:
        '''
        檢查垂直
        '''
        for qx, qy in queens:
            if qy == y and (qx, qy) != (x, y):
                return False
        return True
    def checkBevel(self, x: int, y: int, n: int, queens: List[tuple]) -> bool:
        '''
        檢查斜角
        '''
        #往上找
        angle = 1
        for i in range(1, y + 1):
            if (x + angle, y - i) in queens:
                return False
            if (x - angle, y - i) in queens:
                return False
            angle +=1
        #往下找
        angle = n - y - 1
        for i in range(n - y - 1, 0, -1):
            if (x + angle, y + i) in queens:
                return False
            if (x - angle, y + i) in queens:
                return False
            angle -=1
        return True
    def checkQueen(self, x: int, y: int, n: int, queens: List[tuple]) -> bool:
        return self.checkHorizontal(x, y, queens) and self.checkVertical(x, y, queens) \
            and self.checkBevel(x, y, n, queens)
    def isPassQueens(self, n: int, queens: List[tuple])-> bool:
        for (x, y) in queens:
            if not self.checkQueen(x, y, n, queens):
                return False
        return True
    def buildBoard(self, queens: List[tuple], n: int) -> List[str]: 
        checkerboard = [['.'] * n for _ in range(n)]
        for (i, j) in queens:
            checkerboard[j][i] = 'Q'
        for i in range(n):
            checkerboard[i] = ''.join(checkerboard[i])
        return checkerboard
    def checkRowQueen(self, y: int, queens: List[tuple]) -> bool:
        '''
        檢查是否每行都有棋子
        '''
        allY = [qy for qx, qy in queens]
        return sorted(allY) == list(range(y))
    def nQueens(self, x: int, y: int, queens: List[tuple], n: int) -> List[List[str]]:
        if not self.checkRowQueen(y, queens):
            return []
        if len(queens) != n and (x >= n or y >= n or (x == n - 1 and y == n - 1)):
            return []
        if not self.isPassQueens(n, queens) :
            return []
        if len(queens) == n:
            return [self.buildBoard(queens, n)]
        newX = x + 1
        newY = y
        if newX == n:
            newY += 1
            newX = 0
        return self.nQueens(-1, newY + 1, queens + [(newX, newY)], n) + self.nQueens(newX, newY, queens, n)
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.nQueens(-1, 0, [], n)

tttt = Solution()
nnn = 9
aaa = tttt.solveNQueens(nnn)
for i in range(len(aaa)):
    for j in range(nnn):
        print(aaa[i][j])
    print()


