from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
             return 0
        a = 1#上一次 比如 121 找 12
        b = 1#上上一次 比如 121 找 1
        n = len(s)
        for i in range(1, n):
            if s[i] == '0':
                 a = 0#等於零時, 直接由 b 決定, 且不是 10 20 時 把 b 清零這樣答案就是 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                a = a + b
                b = a - b
            else:#如果單獨等於 7 8 9 等等的直接更新
                b = a#因偉指可能只有一種可能 所以兩個值當成一樣
        return a


tttt = Solution()
print(tttt.numDecodings("12171212126"))
#print(tttt.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))