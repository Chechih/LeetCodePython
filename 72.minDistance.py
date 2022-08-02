from typing import List

class Solution:
    def buildTable(self, n: int, m: int) -> List[List[int]]:
        rlt = []
        for i in range(n + 1):
            rlt.append([0] * (m + 1))
        return rlt
    def minDistance(self, word1: str, word2: str) -> int:
        word1Leg = len(word1)
        word2Leg = len(word2)
        table = self.buildTable(word1Leg, word2Leg)
        for i in range(word1Leg):#因為等於 0 時, 代表另一個字串換過去空字串只需要相同長度的步驟, 也就是全部插入
            table[i + 1][0] = i + 1
        for i in range(word2Leg):
            table[0][i + 1] = i + 1
        #table[0][0] = 0#因為空字串到空字串不需要動
        for i in range(word1Leg):
            for j in range(word2Leg):
                if word1[i] ==  word2[j]:
                    table[i + 1][j + 1] = table[i][j]
                else:
                    table[i + 1][j + 1] = min(
                        table[i + 1][j],#插入
                        table[i][j + 1],#刪除
                        table[i][j]#取代
                        ) + 1
        return table[word1Leg][word2Leg]

tttt = Solution()
print(tttt.minDistance("intention", "execution"))
