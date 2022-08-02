class Solution:
    def isPalindromicSubstring(self, s: str) -> str:
        chars = list(s)
        charsCount = len(chars)
        for i in range(0, int(charsCount/ 2)):
            if(chars[i] != chars[charsCount - 1 - i]):# 只要左右有不合的直接跳出
                return False
        return True
    def numberIsNegative(self, x: int) -> bool:
        return x < 0
    def isPalindrome(self, x: int) -> bool:
        if(self.numberIsNegative(x)):
            return False
        strNum = str(x)
        return self.isPalindromicSubstring(strNum)
