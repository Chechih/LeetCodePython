from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lInd = 0
        numsCount = len(nums)
        rInd = numsCount -1
        if(numsCount > 2):
            while(abs(lInd - rInd) != 1):
                middleInd = int((lInd + rInd)/ 2)
                if(nums[middleInd] < target):
                    lInd = middleInd
                else:
                    rInd = middleInd
        if(rInd == numsCount - 1 and nums[rInd] < target):
            return rInd + 1
        if(lInd == 0 and nums[0] >= target):
            return 0
        return rInd

tttt = Solution()
print(tttt.searchInsert([1,2], 1))
