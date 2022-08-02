from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkBST(self, node: Optional[TreeNode], parentVal = []) -> bool:
        val = node.val
        leftNode = node.left
        if leftNode and (leftNode.val >= val or\
            not self.checkBST(leftNode, parentVal + [('left', val)])):#檢查左邊
            return False
        rightNode = node.right
        if rightNode and (rightNode.val <= val or \
            not self.checkBST(rightNode, parentVal + [('right', val)])):#檢查右邊
            return False
        if not leftNode and not rightNode:#到最底時檢查上面所有節點是否符合規則
            for pd, pv in parentVal:
                if (pd == 'left' and val >= pv) or \
                    (pd == 'right' and val <= pv):
                    return False         
        return True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root)


tttt = Solution()
a1 = TreeNode(1)
a3 = TreeNode(3)
a2 = TreeNode(2, a1, a3)

print(tttt.isValidBST(a2))     