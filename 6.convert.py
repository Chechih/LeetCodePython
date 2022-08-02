class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):#測試可能會只有一 直接回傳
            return s
        roundRule = 2* numRows - 2#會有幾個波型
        strCount = len(s)#自圓長度
        newStr = ''#回傳值
        maxRound = int(strCount / roundRule) + 2
        for i in range(0, numRows):
            for j in range(0, maxRound):
                if(i == 0):#最上面
                    if(roundRule * j < strCount):
                        newStr = newStr + s[roundRule * j]
                elif(i == numRows - 1):#最下面
                    if(roundRule * j + roundRule / 2 < strCount):
                        newStr = newStr + s[roundRule * j + int(roundRule / 2)]
                else:#中間部分
                    if(roundRule * j - i > 0 and roundRule * j - i < strCount):#中間部分可能多 i
                        newStr = newStr + s[roundRule * j - i]
                    if(roundRule * j + i > 0 and roundRule * j + i < strCount):#少 i
                        newStr = newStr + s[roundRule * j + i]
        return newStr

tttt = Solution();
print(tttt.convert("ABCDE", 4))
