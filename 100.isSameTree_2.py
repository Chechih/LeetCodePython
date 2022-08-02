from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q) or (p and q and p.val != q.val):
            return False
        if ((p && !q) || (!p && q) || (p->val != q->val)) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);



tttt = Solution()
a4 = TreeNode(4)
a2 = TreeNode(2, None, a4)

b3 = TreeNode(3)
b4 = TreeNode(4)
b2 = TreeNode(2, b3, b4)

print(tttt.isSameTree(a2, b2))     