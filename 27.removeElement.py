from typing import List
from typing import Optional

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) -1, -1, -1):#因為正循環移除會破壞迴圈的數目
            if(nums[i] == val):
                nums.pop(val)
        return  len(nums)