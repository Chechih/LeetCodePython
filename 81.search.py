from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        sortNums = sorted(nums)
        return target in sortNums