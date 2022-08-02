class Solution:
    def mathSqrt(self, left, right, x: int) -> int:
        '''
        切兩段下去找平方根
        '''
        add = (left + right + 1) // 2
        pow2Add = add ** 2
        if pow2Add <= x:
            if (add + 1) ** 2 > x or pow2Add == x:
                return add
            return self.mathSqrt(add, right, x)
        return self.mathSqrt(left, add, x)
    def mySqrt(self, x: int) -> int:
        return self.mathSqrt(0, x, x)


tttt = Solution()
print(tttt.mySqrt(24))