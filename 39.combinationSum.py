from typing import List
import copy

class Solution:
    def findCombinationSum(self, candidates: List[int], target: int, candidatesInd: int, thisVal: List[int], rlt: List[List[int]]) -> None:
        thisValSum = sum(thisVal)
        if(thisValSum == target):
            rlt.append(copy.copy(thisVal))
        for i in range(candidatesInd, len(candidates)):
            if(thisValSum + candidates[i] > target):
                return
            thisVal.append(candidates[i])
            self.findCombinationSum(candidates, target, i, thisVal, rlt)
            thisVal.pop()
        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rlt = []
        candidates.sort()
        self.findCombinationSum(candidates, target, 0, [], rlt)
        return rlt

tttt = Solution()
print(tttt.combinationSum([2,3,5], 8))