class Solution:
    maxNum = 2147483648
    minNum = -2147483648
    def initMultiple(self, dividend: int, divisor: int) -> object:
        multiples = {}
        isExceed = False
        nowVal = divisor
        count = 1
        while(not isExceed):
            if(dividend >= nowVal):
                multiples[nowVal] = count
                nowVal = nowVal + nowVal
                count = count + count
            else:
                isExceed = True
        return multiples
    def into32bit(self, num: int) -> int:
        if(num >= self.maxNum):
            num = self.maxNum - 1
        elif(num <= self.minNum):
            num = self.minNum
        return num
    def divide(self, dividend: int, divisor: int) -> int:
        divisorIsNegativeNum = divisor < 0
        dividendIsNegativeNum = dividend < 0
        if(divisorIsNegativeNum):
            divisor = abs(divisor)
        if(dividendIsNegativeNum):
            dividend = abs(dividend)
        multiples = self.initMultiple(dividend, divisor)
        rlt = 0
        reversedKeys = list(reversed(sorted(multiples.keys())))
        for mk in reversedKeys:
            mv = multiples[mk]
            if(dividend >= mk):
                dividend -= mk
                rlt += mv
        if((divisorIsNegativeNum and not dividendIsNegativeNum) or
        (dividendIsNegativeNum and not divisorIsNegativeNum)):
            rlt = int('-' + str(rlt))
        return self.into32bit(rlt)


tttt = Solution()
print(tttt.divide(-2147483648, 1))

