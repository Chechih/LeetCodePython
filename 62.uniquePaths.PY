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
    def uniquePaths(self, m: int, n: int) -> int:
        return self.mathC(m + n - 2, min(m, n) - 1)