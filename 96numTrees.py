from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    numTreesDict = {0: 0, 1: 1, 2: 2, 3: 5}
    def buildGenerateTree(self, n: int) -> int:
        numTreesDict = self.numTreesDict
        rlt = 0
        for i in range(0, n):
            more = n - 1 - i #大於
            less = i #小於
            tnsMore = numTreesDict[more] or 1
            tnsLess = numTreesDict[less] or 1
            rlt += tnsMore * tnsLess
        return rlt
    def numTrees(self, n: int) -> int:
        numTreesDict = self.numTreesDict
        for i in range(1, n + 1):
            if not i in numTreesDict:
                numTreesDict[i] = self.buildGenerateTree(i)
        return numTreesDict[n]


tttt = Solution()
print(tttt.numTrees(4))   