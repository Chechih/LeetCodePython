from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def swapTreeNode(p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
        temp = p.val
        p.val = q.val
        q.val = temp
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second, cur, pre = None, None, root, None
        while cur:
            if cur.left:
                p = cur.left
                while p.right and p.right is not cur:
                     p = p.right
                if not p.right:
                    p.right = cur
                    cur = cur.left
                    continue
                else:
                    p.right = None
            if pre and cur.val < pre.val:
                if not first:
                    first = pre
                second = cur
            pre = cur
            cur = cur.right
        self.swapTreeNode(first, second)