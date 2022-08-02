from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        rlt = []
        leftAry = []
        def findLastLeftNode(root: Optional[TreeNode]) -> TreeNode:
            r = root
            while r.left:
                leftAry.append(r)
                r = r.left
            return r
        def findLeftAllNode(lastLeft: Optional[TreeNode]) -> None:
            while lastLeft:
                rlt.append(lastLeft.val)
                while lastLeft.right:
                    lastLeft = lastLeft.right
                    lastLeft = findLastLeftNode(lastLeft)
                    rlt.append(lastLeft.val)
                if leftAry:
                    lastLeft = leftAry.pop()
                else:
                    lastLeft = None
        lastLeft = findLastLeftNode(root)
        findLeftAllNode(lastLeft)
        return rlt
            
tttt = Solution()
a1 = TreeNode(1)
a3 = TreeNode(3)
a2 = TreeNode(2, a1, a3)
a8 = TreeNode(8)
a6 = TreeNode(6, None, a8)
a5 = TreeNode(5, a2, a6)

print(tttt.inorderTraversal(a5))      
        
