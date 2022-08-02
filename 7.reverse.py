class Solution:
    maxNum = 2147483648
    minNum = -2147483648
    def numberIsNegative(self, x: int) -> bool:
        return x < 0
    def reverse(self, x: int) -> int:
        absNum = abs(x)
        strNum = str(absNum)
        reversedStrNum = ''.join(reversed(strNum))
        rlt = -1 * int(reversedStrNum) if(self.numberIsNegative(x)) else int(reversedStrNum)
        # if(self.numberIsNegative(x)) -1 * int(reversedStrNum) else int(reversedStrNum)
        return rlt if(rlt < self.maxNum and rlt > self.minNum) else 0

tttt = Solution()
print(tttt.reverse(1534236469))