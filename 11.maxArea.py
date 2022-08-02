from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxRect = 0
        heightCount = len(height)
        lInd = 0
        rInd = heightCount -1
        while(lInd < rInd):
            lVal = height[lInd]
            rVal = height[rInd]            
            maxRect = max(maxRect, abs(lInd - rInd) * min(lVal, rVal))
            if(lVal < rVal):
                lInd += 1
            else:
                rInd -= 1

        return maxRect

tttt = Solution()
tttt.maxArea([1,8,6,2,5,4,8,3,7])