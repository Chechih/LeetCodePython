from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return None
        rlt = []
        leftAry = []
        def findLastLeftNode(root: Optional[TreeNode]) -> TreeNode:
            r = root
            while r.left != None:
                leftAry.append(r)
                r = r.left
            return r
        def findLeftAllNode(lastLeft: Optional[TreeNode]) -> None:
            while lastLeft != None:
                rlt.append(lastLeft)
                while lastLeft.right != None:
                    lastLeft = lastLeft.right
                    lastLeft = findLastLeftNode(lastLeft)
                    rlt.append(lastLeft)
                if leftAry:
                    lastLeft = leftAry.pop()
                else:
                    lastLeft = None
        lastLeft = findLastLeftNode(root)
        findLeftAllNode(lastLeft)
        return rlt
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorderTraversalAry = self.inorderTraversal(root)
        allVal = [it.val for it in inorderTraversalAry]
        allVal.sort()
        for i, ita in enumerate(inorderTraversalAry):
            ita.val = allVal[i]