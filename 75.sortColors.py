from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for n in nums:
            if n == 0:
                zeros += 1
            if n == 1:
                ones += 1
            if n == 2:
                twos += 1    
        nums.clear()      
        nums.extend([0] * zeros + [1] * ones + [2] * twos)

tttt = Solution()
#print(tttt.sortColors([2,1,0]))
#print(tttt.sortColors([2,0,1]))
print(tttt.sortColors([2,1,2]))
print(tttt.sortColors([1,2,0]))
print(tttt.sortColors([1,2,1]))