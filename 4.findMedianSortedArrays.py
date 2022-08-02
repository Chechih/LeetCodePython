import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        allNums = nums1 + nums2;
        allNums = sorted(allNums);
        numCount = len(allNums) - 1;
        middle = numCount / 2;
        if(int(middle) == middle):
            return allNums[int(middle)];
        else:
            ceil =  allNums[int(math.ceil(middle))];
            floor = allNums[int(math.floor(middle))];
            return (ceil + floor) / 2;

ttt = Solution();
print(ttt.findMedianSortedArrays([1,3], [2]));