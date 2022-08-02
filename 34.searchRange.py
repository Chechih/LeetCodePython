from typing import List
from collections import Counter

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target in nums):
            startInd = nums.index(target)
            numsCounter = Counter(nums)
            return [startInd, startInd + numsCounter[target] - 1]
        return [-1, -1]