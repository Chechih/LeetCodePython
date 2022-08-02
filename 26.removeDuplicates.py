from typing import List
from typing import Optional

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newNums = sorted(list(set(nums)))#留下不重複的並排序
        del nums[:] #清除所有元素
        nums += newNums #合併兩個 array

        return len(newNums)


tttt = Solution()
print(tttt.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))