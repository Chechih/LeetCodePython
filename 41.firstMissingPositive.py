from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        maxRule = max(nums)+ 2 if( max(nums)+ 2 < 2147483647) else 500000
        rule = list(range(1, maxRule))
        diff = list(set(rule) - set(nums))
        if(len(diff) > 0):
            return min(diff)
        else:
            return 1

tttt = Solution()
print(tttt.firstMissingPositive([1,2,0, 2147483647]))