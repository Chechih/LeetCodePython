from typing import List
import copy

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.從陣列最右邊開始一個個搜尋，若是第 i 個值比第 i+1 個值來得更小，
        #   則從 i 開始往右側找尋比『第 i 個值』大的值當中的『最小值』
        # 2.交換第 i 個值以及比第 i 個值大的最小值
        # 3.從原本 i 的位置往右，將全部的值從最小到最大排序
        # 4.如此一來，我們就能得到『下一個較大的排列』
        copyNums = copy.copy(nums)
        copyNums.sort()
        copyNums.reverse()
        if(copyNums == nums):
            nums.sort()
            return
        for i in range(len(nums) -1, -1, -1):
            iNum = nums[i]
            if(i + 1 < len(nums) and iNum < nums[i + 1]):
                minMax = None
                moreiNum = nums[i + 1]
                moreiNumInd = i + 1
                for j in range(i + 1, len(nums)):
                    jNum = nums[j]
                    if (jNum > iNum and moreiNum > jNum):
                        moreiNum = jNum
                        moreiNumInd = j
                nums[i], nums[moreiNumInd] = nums[moreiNumInd], nums[i]
                sortIafter = sorted(nums[i+1: len(nums)])
                for j in range(i+1, len(nums)):
                    nums[j] = sortIafter[j - i - 1]
                break
        return

tttt = Solution()
print(tttt.nextPermutation([1,3,2]))  #[2,1,3]