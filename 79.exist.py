from typing import List, Tuple

class Solution:
    def searchWord(self, board: List[List[str]], word: str, ind: Tuple[int, int]) -> bool:
        if not word:
            return True
        x = ind[0]
        y = ind[1]
        if y - 1 >= 0 and board[y - 1][x] == word[0]:
            board[y - 1][x] = None
            if self.searchWord(board, word[1:], (x, y - 1)):
                return True
            board[y - 1][x] = word[0]
        if x - 1 >= 0 and board[y][x - 1] == word[0]:
            board[y][x - 1] = None
            if self.searchWord(board, word[1:], (x - 1, y)):
                return True
            board[y][x - 1] = word[0]
        if y + 1 < len(board) and board[y + 1][x] == word[0]:
            board[y + 1][x] = None
            if self.searchWord(board, word[1:], (x, y + 1)):
                return True 
            board[y + 1][x] = word[0]
        if x + 1 < len(board[0]) and board[y][x + 1] == word[0]:
            board[y][x + 1] = None
            if self.searchWord(board, word[1:], (x + 1, y)):
                return True       
            board[y][x + 1] = word[0]     
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = None
                    if self.searchWord(board, word[1:], (j, i)):
                        return True
                    board[i][j] = word[0]
        return False


tttt = Solution()
print(tttt.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "ABCCED"))
