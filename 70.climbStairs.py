class Solution:
    def getFactorial(self, n: int) -> int:
        rlt = 1
        for i in range(1, n + 1):
            rlt *= i
        return rlt
    def mathP(self, cn: int, cm: int) -> int:
        rlt = 1
        for i in range(cn, cm, -1):
            rlt *= i
        return rlt
    def mathC(self, cn: int, cm: int) -> int:
        p = self.mathP(cn, cm)
        return p //  self.getFactorial(cn - cm)
    def climbStairs(self, n: int) -> int:
        rlt = 0
        steps1 = n
        steps2 = 0
        for i in range((n // 2 + 1)):
            steps2 = i
            steps1 = n - 2 * steps2
            rlt += self.mathC(steps1 + steps2, steps2)
        return rlt

tttt = Solution()
print(tttt.climbStairs(4))