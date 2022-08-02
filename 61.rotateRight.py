from typing import Optional
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def head2List(self, head) -> List[ListNode]:
        rlt = [];
        h = head;
        while h is not None:
            rlt.append(h);
            h = h.next;
        return rlt;
    def displacementHeadAry(self, headAry: List[ListNode], k: int) -> List[ListNode]:
        headLeg = len(headAry)
        for i in range(k):
            temp = headAry[headLeg - 1]
            headAry.remove(temp)
            headAry.insert(0, temp)
        return headAry
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        headAry = self.head2List(head)
        headLeg = len(headAry)
        if headLeg == 0:
            return None
        k %= headLeg
        rlt = headAry[0]
        if headLeg > 0:
            headAry[headLeg - 1].next = headAry[0]
            headAry = self.displacementHeadAry(headAry, k)
            rlt = headAry[0]
            headAry[headLeg - 1].next = None
        return rlt
