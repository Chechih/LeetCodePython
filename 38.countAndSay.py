class Solution:
    def callCountAndSay(self, n: int) -> str:
        if(n == 1):
            return '1'
        else:
            rlt = ''
            previous = self.callCountAndSay(n - 1)
            thisVal = previous[0]
            strCount = 0
            for s in previous:
                if(thisVal == s):
                    strCount += 1
                else:
                    rlt += str(strCount) + thisVal
                    thisVal = s
                    strCount = 1
            rlt += str(strCount) + thisVal
            return rlt

    def countAndSay(self, n: int) -> str:
        return self.callCountAndSay(n)


tttt = Solution()
print(tttt.callCountAndSay(5))