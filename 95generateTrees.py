from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildGenerateTree(self, nodes: List[int]) -> List[Optional[TreeNode]]:
        rlt = []
        for n in nodes:
            cloneNodes = nodes.copy()
            cloneNodes.remove(n)
            cloneNodes.sort()
            more = [m for m in cloneNodes if m >= n] #大於
            tnsMore = self.buildGenerateTree(more)
            less = [l for l in cloneNodes if l < n] #小於
            tnsLess = self.buildGenerateTree(less)
            if tnsMore and tnsLess:
                for mn in tnsMore:
                    for ln in tnsLess:
                        indNode = TreeNode(n)
                        indNode.right = mn
                        indNode.left = ln
                        rlt.append(indNode)
            elif tnsMore:
                for mn in tnsMore:
                    indNode = TreeNode(n)
                    indNode.right = mn
                    rlt.append(indNode)
            elif tnsLess:
                for ln in tnsLess:
                    indNode = TreeNode(n)
                    indNode.left = ln
                    rlt.append(indNode)      
            else:
                rlt.append(TreeNode(n))          
        return rlt
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nodes = list(range(1, n + 1))
        rlt = self.buildGenerateTree(nodes)
        return rlt


tttt = Solution()
print(tttt.generateTrees(8))   