from typing import List
from collections import Counter
import copy

class Solution:
    def checkSudokuHorizontal(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hb = board[i]
            hbCounter = Counter(hb)
            del hbCounter['.']
            hbCounterVals = hbCounter.values()
            if(len(hbCounterVals) < 1): #因為可能船全部 '.' 進來
                continue #因為不一定要能解開 所以全部白也算是可以解的
            if(max(hbCounterVals) > 1):
                return False
        return True
    def checkSudokuVertical(self, board: List[List[str]]) -> bool:
        vss = [[],[],[],[],[],[],[],[],[]]
        for i in range(len(board)):
            for j in range(len(board)):
                vss[i].append(board[j][i])
        return self.checkSudokuHorizontal(vss)
    def checkSudokuSquare(self, board: List[List[str]]) -> bool:
        sss = [
            [board[0][0],board[1][0],board[2][0],board[0][1],board[1][1],board[2][1],board[0][2],board[1][2],board[2][2]],
            [board[0][3],board[1][3],board[2][3],board[0][4],board[1][4],board[2][4],board[0][5],board[1][5],board[2][5]],
            [board[0][6],board[1][6],board[2][6],board[0][7],board[1][7],board[2][7],board[0][8],board[1][8],board[2][8]],
            [board[3][0],board[4][0],board[5][0],board[3][1],board[4][1],board[5][1],board[3][2],board[4][2],board[5][2]],
            [board[3][3],board[4][3],board[5][3],board[3][4],board[4][4],board[5][4],board[3][5],board[4][5],board[5][5]],
            [board[3][6],board[4][6],board[5][6],board[3][7],board[4][7],board[5][7],board[3][8],board[4][8],board[5][8]],
            [board[6][0],board[7][0],board[8][0],board[6][1],board[7][1],board[8][1],board[6][2],board[7][2],board[8][2]],
            [board[6][3],board[7][3],board[8][3],board[6][4],board[7][4],board[8][4],board[6][5],board[7][5],board[8][5]],
            [board[6][6],board[7][6],board[8][6],board[6][7],board[7][7],board[8][7],board[6][8],board[7][8],board[8][8]]]
        return self.checkSudokuHorizontal(sss)
    def removeEleInAnotherArray(self, ary: List[List[str]], removeEle: List[str]) -> List[str]:
        return [x for x in ary if x not in removeEle]
    def initSudokuHorizontalAnswer(self, board: List[List[str]]) -> object:
        possibilityAnswer ={}
        for i in range(len(board)):
            hb = board[i]
            hbCounter = Counter(hb)
            del hbCounter['.']
            hbCounterKeys = hbCounter.keys()
            for j in range(len(hb)):
                if(hb[j] == '.'):
                    possibilityAnswer[(i, j)] = self.removeEleInAnotherArray(
                        ['1', '2', '3', '4', '5', '6', '7', '8', '9'], list(hbCounterKeys))
        return possibilityAnswer
    def initSudokuVerticalAnswer(self, board: List[List[str]]) -> object:
        vss = [[],[],[],[],[],[],[],[],[]]
        possibilityAnswer ={}
        for i in range(len(board)):
            for j in range(9):
                if(board[j][i] != '.'):
                    vss[i].append(board[j][i])
            for j in range(len(board)):
                if(board[j][i] == '.'):
                    possibilityAnswer[(j, i)] = self.removeEleInAnotherArray(
                        ['1', '2', '3', '4', '5', '6', '7', '8', '9'], list(vss[i]))
        return possibilityAnswer
    def initSudokuSquareAnswer(self, board: List[List[str]]) -> object:
        sss = [
            [board[0][0],board[1][0],board[2][0],board[0][1],board[1][1],board[2][1],board[0][2],board[1][2],board[2][2]],
            [board[0][3],board[1][3],board[2][3],board[0][4],board[1][4],board[2][4],board[0][5],board[1][5],board[2][5]],
            [board[0][6],board[1][6],board[2][6],board[0][7],board[1][7],board[2][7],board[0][8],board[1][8],board[2][8]],
            [board[3][0],board[4][0],board[5][0],board[3][1],board[4][1],board[5][1],board[3][2],board[4][2],board[5][2]],
            [board[3][3],board[4][3],board[5][3],board[3][4],board[4][4],board[5][4],board[3][5],board[4][5],board[5][5]],
            [board[3][6],board[4][6],board[5][6],board[3][7],board[4][7],board[5][7],board[3][8],board[4][8],board[5][8]],
            [board[6][0],board[7][0],board[8][0],board[6][1],board[7][1],board[8][1],board[6][2],board[7][2],board[8][2]],
            [board[6][3],board[7][3],board[8][3],board[6][4],board[7][4],board[8][4],board[6][5],board[7][5],board[8][5]],
            [board[6][6],board[7][6],board[8][6],board[6][7],board[7][7],board[8][7],board[6][8],board[7][8],board[8][8]]]
        sssKeys = [
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)], 
            [(0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)], 
            [(0, 6), (1, 6), (2, 6), (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8)], 
            [(3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2)], 
            [(3, 3), (4, 3), (5, 3), (3, 4), (4, 4), (5, 4), (3, 5), (4, 5), (5, 5)], 
            [(3, 6), (4, 6), (5, 6), (3, 7), (4, 7), (5, 7), (3, 8), (4, 8), (5, 8)], 
            [(6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2)], 
            [(6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5)], 
            [(6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8)]]
        ssa = [[],[],[],[],[],[],[],[],[]]
        possibilityAnswer ={}
        for i in range(9):
            for j in range(9):
                if(sss[i][j] != '.'):
                    ssa[i].append(sss[i][j])
            for j in range(9):
                if(sss[i][j] == '.'):
                    possibilityAnswer[sssKeys[i][j]] = self.removeEleInAnotherArray(
                        ['1', '2', '3', '4', '5', '6', '7', '8', '9'], list(ssa[i]))
        return possibilityAnswer
    def initPossibilityAnswer(self, board: List[List[str]])-> object:
        possibilityAnswer = {}
        hsPossibilityAnswer = self.initSudokuHorizontalAnswer(board)
        vsPossibilityAnswer = self.initSudokuVerticalAnswer(board)
        ssPossibilityAnswer = self.initSudokuSquareAnswer(board)  
        possibilityAnswerKeys = hsPossibilityAnswer.keys()
        for i in possibilityAnswerKeys:
            possibilityAnswer[i] = list(set(hsPossibilityAnswer[i]) 
            & set(vsPossibilityAnswer[i])
            & set(ssPossibilityAnswer[i]))
        return possibilityAnswer
    def checkAnswer(self, possibilityAnswer: object, board: List[List[str]]) -> bool:
        if(not self.checkSudokuHorizontal(board) or not self.checkSudokuVertical(board) or not self.checkSudokuSquare(board)):
            return False
        for i in possibilityAnswer:
            possibilityVals = possibilityAnswer[i]
            x, y = i
            if(board[x][y] == '.'):
                copyPossibilityAnswer = copy.copy(possibilityAnswer)
                del copyPossibilityAnswer[i]
                for j in possibilityVals:
                    board[x][y] = str(j)
                    if self.checkAnswer(copyPossibilityAnswer, board):
                        return True
                    board[x][y] = '.'
                return False
        return True
                
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        possibilityAnswer = self.initPossibilityAnswer(board)
        self.checkAnswer(possibilityAnswer, board)
        return

board = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
tttt = Solution()
tttt.solveSudoku(board)   
a=1