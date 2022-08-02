from typing import List
import numpy as np

class Solution:
    def trap(self, height: List[int]) -> int:
        heightCount = len(height)
        leftHeight = [0] * heightCount#存每個點的左邊
        rightHeight = [0] * heightCount#存每個點的右邊
        leftHeight[0] = height[0]
        rightHeight[heightCount - 1] = height[heightCount - 1]

        for i in range(1, heightCount):#先找出所有的左邊
            leftHeight[i] = max(leftHeight[i - 1], height[i])

        for i in range(heightCount - 2, -1, -1):#再找出所有的右邊
            rightHeight[i] = max(height[i], rightHeight[i + 1])   
            
        return np.sum(np.minimum(leftHeight, rightHeight) -  np.array(height))

tttt = Solution()
print(tttt.trap([0,1,0,2,1,0,1,3,2,1,2,1]))