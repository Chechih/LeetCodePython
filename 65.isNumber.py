class Solution:
    def isDecimalPointNum(self, s: str) -> bool:
        if '.' in s:#有小數點
            decimalPoint = s.split('.')
            if len(decimalPoint) != 2:#小數點只有兩段
                return False
            first = decimalPoint[0]
            last = decimalPoint[1]
            if first == '' and last == '':#'.' '3.'
                return False
            return self.isIntegerNum(first) and self.isIntegerNum(last)
        return False
    def isIntegerNum(self, s: str) -> bool:
        for sd in s:
            if not sd.isdigit():
                return False
        return True
    def isEulerNum(self, s: str) -> bool:
        s = s.replace('E', 'e').replace('e+', 'e').replace('e-', 'e')
        if 'e' in s:
            eulerNum = s.split('e')
            if len(eulerNum) != 2:
                return False
            first = eulerNum[0]
            last = eulerNum[1]
            if first == '' or last == '':
                return False
            return (self.isDecimalPointNum(first) or self.isIntegerNum(first)) and self.isIntegerNum(last)
        return False
    def isPositiveNegativeNumber(self, s: str) -> bool:
        s = s.replace('E', 'e').replace('e+', 'e').replace('e-', 'e')
        positive = '+' in s
        negative = '-' in s
        firstNum = s[0]
        sLeg = len(s)
        if positive and firstNum == '+' and not negative and sLeg > 1:#有正號不能有負號
            return True
        elif negative and firstNum == '-' and not positive and sLeg > 1:#有負號不能有正號
            return True
        elif not positive and not negative:#都沒有
            return True
        return False
    def isFirstPositiveNegative(self, s: str) -> bool:
        firstNum = s[0]
        return firstNum == '+' or firstNum == '-'
    def isNumber(self, s: str) -> bool:
        s = s.replace(' ', '')
        if not self.isPositiveNegativeNumber(s):
            return False
        if self.isFirstPositiveNegative(s):
            s = s[1:]
        return self.isDecimalPointNum(s) or self.isEulerNum(s) or self.isIntegerNum(s)

tttt = Solution()
#print(tttt.isNumber('005047e+6'))

print(tttt.isNumber("+"))