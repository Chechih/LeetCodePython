from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        thisNum = None
        time = 1
        removeAry = []
        for n in nums:
            if thisNum == n:
                time += 1
            else:
                thisNum = n
                time = 1
            if time > 2:
                removeAry.append(n)
        for ra in removeAry:
            nums.remove(ra)
        return len(nums)

tttt = Solution()
print(tttt.removeDuplicates([1,1,1,2,2,3]))
