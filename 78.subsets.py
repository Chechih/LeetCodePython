from typing import List

class Solution:
    def getSubsets(self, nums: List[int], level: int = 0, res: List[int] = []) -> List[tuple]:
        rlt = []
        loop = nums[level:]
        for i in loop:
            if not i in res and (not res or i > max(res)):
                #如果現在的數字家道後面比 n 大直接不跑遞迴了
                #如果筆最大的樹小也不跑
                cloneRes = res + [i]
                rlt.append(cloneRes)
                combines = self.getSubsets(nums, level + 1, res + [i])
                rlt = rlt + combines
        return rlt
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        rlt = self.getSubsets(nums)
        return [[]] + rlt

tttt = Solution()
print(tttt.subsets([1,2,3]))