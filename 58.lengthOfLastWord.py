class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() #移除開頭結尾的空格
        sLeg = len(s)
        if(sLeg < 1):
            return 0
        rlt = 0
        for i in range(sLeg - 1, -1, -1):
            sss = s[i]
            if sss != ' ':
                rlt += 1
            else:
                return rlt
        return rlt

tttt = Solution()
print(tttt.lengthOfLastWord(
"Hello World"))