
class Solution(object):
    def twoSum(self, nums, target):
        iNumsCount = len(nums);
        rlt = [-1, -1];
        for i in range(0, iNumsCount): 
            numVal = nums[i];
            differ = target - numVal;
            ind = -1;
            if(differ in nums):
                ind = nums.index(differ);
                if(ind != i):
                    rlt = [i, ind];
                    break;
        return rlt;


tttt = Solution();
tttt.twoSum([3,2,4], 6);