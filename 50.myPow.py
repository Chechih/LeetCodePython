
class Solution:
    def mathPow(self, x: float, n: int) -> float:
        if(n == 1):
            return x
        elif(n == -1):
            return 1 / x
        elif(n == 0):
            return 1
        elif(n % 2 == 0):
            half = self.mathPow(x, int(n /2))
            return half * half
        return self.mathPow(x, n -1) * x
    def myPow(self, x: float, n: int) -> float:
        return self.mathPow(x, n)


tttt = Solution()
print(tttt.myPow(2.00000, -2))