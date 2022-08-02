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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pCur, pPre = p, None
        qCur, qPre = q, None

        while pCur:
            if (not pCur and qCur) or (pCur and not qCur) or (pCur and qCur and pCur.val != qCur.val) or\
                    (not pPre and qPre) or (pPre and not qPre) or (pPre and qPre and pPre.val != qPre.val):
                return False
            if not pCur.left:
                if qCur and qCur.left:
                    return False
                pCur = pCur.right
                qCur = qCur.right
            else:
                pPre = pCur.left
                qPre = qCur.left
                while pPre.right and pPre.right is not pCur:
                    pPre = pPre.right
                while qPre and qPre.right and qPre.right is not qCur:
                    qPre = qPre.right
                if not pPre.right:
                    pPre.right = pCur#利用這邊回去中結點
                    pCur = pCur.left
                    if not qPre or not qCur:
                        return False
                    qPre.right = qCur
                    qCur = qCur.left
                else:
                    pPre.right = None#清掉中結點
                    pCur = pCur.right
                    if not qPre or not qCur:
                        return False
                    qPre.right = None
                    qCur = qCur.right
        if (not pCur and qCur) or (pCur and not qCur) or (pCur and qCur and pCur.val != qCur.val) or\
                (not pPre and qPre) or (pPre and not qPre) or (pPre and qPre and pPre.val != qPre.val):
            return False
        return True



tttt = Solution()
a4 = TreeNode(4)
a2 = TreeNode(2, None, a4)

b3 = TreeNode(3)
b4 = TreeNode(4)
b2 = TreeNode(2, b3, b4)

print(tttt.isSameTree(a2, b2))     