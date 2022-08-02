from typing import List
import copy

class Solution:
    def findCombinationSum(self, candidates: List[int], numsCount, thisVal: List[int], rlt: List[List[int]]) -> None:
        if(len(thisVal) == numsCount):
            rlt.append(copy.copy(thisVal))
        for i in range(0, len(candidates)):
            thisVal.append(candidates[i])
            candidatesCopy = copy.copy(candidates)
            candidatesCopy.remove(candidates[i])
            self.findCombinationSum(candidatesCopy, numsCount, thisVal, rlt)
            thisVal.pop()
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        rlt = []
        numsCount = len(nums)
        self.findCombinationSum(nums, numsCount, [], rlt)
        return rlt

tttt = Solution()
print(tttt.permute([0,1]))
        