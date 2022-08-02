from typing import List

class Solution:
    def getCombine(self, n: int, k: int, level: int = 0, res: List[int] = []) -> List[tuple]:
        if len(res) == k:
            return [res]
        rlt = []
        for i in range(level + 1, n + 1):
            if not i in res and i + k - len(res) -1 <= n and (not res or i > max(res)):
                #如果現在的數字家道後面比 n 大直接不跑遞迴了
                #如果筆最大的樹小也不跑
                combines = self.getCombine(n, k, level + 1, res + [i])
                rlt = rlt + combines
        return rlt
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.getCombine(n, k)


tttt = Solution()
print(tttt.combine(20,16))
