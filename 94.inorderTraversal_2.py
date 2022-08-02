from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #Morris Traversal
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rlt = []
        cur, pre = root, None

        while cur:
            if not cur.left:
                rlt.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur#利用這邊回去中結點
                    cur = cur.left
                else:
                    pre.right = None#清掉中結點
                    rlt.append(cur.val)
                    cur = cur.right
        return rlt
            
tttt = Solution()
a1 = TreeNode(1)
a3 = TreeNode(3)
a2 = TreeNode(2, a1, a3)
a8 = TreeNode(8)
a6 = TreeNode(6, None, a8)
a5 = TreeNode(5, a2, a6)

print(tttt.inorderTraversal(a5))      
        
