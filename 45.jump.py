from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        numsCount = len(nums)
        stepDict = {}
        if(numsCount == 1):
            return 0
        for i in range(numsCount-1, -1, -1):
            maxMove = nums[i]
            if(i + maxMove >= numsCount -1):
                stepDict[i] = 1
            elif(maxMove == 0):
                stepDict[i] = -1
            else:
                minMove = numsCount -1 - i
                for j in range(1, maxMove +1):
                    if(stepDict[i+j] != -1 and minMove > stepDict[i+j]):
                        minMove = stepDict[i+j] + 1
                stepDict[i] = minMove
        return stepDict[0]


tttt = Solution()
print(tttt.jump([0]))