from typing import List
#https://ithelp.ithome.com.tw/articles/10228245

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numsLeg = len(nums)
        if numsLeg == 0:
            return False
        maxStepCount = 0

        for i in range(numsLeg):
            n = nums[i]
            if maxStepCount < i:#如果最大能走的步數比現在小, 代表有位子卡住
                return False
            maxStepCount = max(maxStepCount, n + i)#檢查每個位子能走的最大步數
        return True