from typing import List

class Solution:
    def getSubsets(self, nums: List[int], rlt: List[int], level: int = 0, res: List[int] = []) -> None:
        loop = nums[level:]
        for i in loop:
            cloneRes = res + [i]
            if nums.count(i) >= res.count(i) + 1 and sorted(cloneRes) == cloneRes:
                if not cloneRes in rlt:
                    rlt.append(cloneRes)
                self.getSubsets(nums, rlt, level + 1, res + [i])
        return rlt
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        rlt = []
        self.getSubsets(nums, rlt)
        return [[]] + rlt


tttt = Solution()
print(tttt.subsetsWithDup([1,2,3]))