from typing import List

class Solution:
    #維基 鏡射排列
    grayCodeList = {1: ['0', '1']}
    def buildGrayCode(self, n: int) -> None:
        grayCodeList = self.grayCodeList
        if n in grayCodeList:
            return
        self.buildGrayCode(n - 1)
        preGC = grayCodeList[n - 1]
        gc = preGC + preGC[::-1]
        gcLeg = len(gc)
        for i in range(gcLeg):
            if i < gcLeg / 2:
                gc[i] = '0' + gc[i]
            else:
                gc[i] = '1' + gc[i]
        grayCodeList[n] = gc

    def grayCode(self, n: int) -> List[int]:
        self.buildGrayCode(n)
        gcL = self.grayCodeList[n]
        return [int(g, 2) for g in gcL]


tttt = Solution()
print(tttt.grayCode(3))