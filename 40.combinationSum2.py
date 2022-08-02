from typing import List
from collections import Counter
import copy

class Solution:
    def findCombinationSum(self, candidatesDict: object, target: int, candidatesInd: int, thisVal: List[int], rlt: List[List[int]]) -> None:
        thisValSum = sum(thisVal)
        if(thisValSum == target):
            rlt.append(copy.copy(thisVal))
            return
        candidatesKeys = list(candidatesDict.keys())
        for i in range(candidatesInd, len(candidatesKeys)):
            key = candidatesKeys[i]
            candidatesDict[key] -= 1
            if(candidatesDict[key] < 0):
                candidatesDict[key] += 1
                continue
            if(thisValSum + key > target):
                candidatesDict[key] += 1
                return
            thisVal.append(key)
            self.findCombinationSum(candidatesDict, target, i, thisVal, rlt)
            candidatesDict[key] += 1
            thisVal.pop()
        return
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        rlt = []
        candidates.sort()
        candidatesDict = Counter(candidates)
        self.findCombinationSum(candidatesDict, target, 0, [], rlt)
        return rlt

tttt = Solution()
print(tttt.combinationSum2([10,1,2,7,6,1,5], 8))