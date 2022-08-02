from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headAry = []
        h = head
        preVal = None
        while h is not None:
            if preVal == h.val:
                if headAry:#一開始有重複時
                    headAry[-1].next = None
            else:
                if headAry and headAry[-1].next == None:#如果最後一個是空的換成新的
                    headAry[-1].next = h
                headAry.append(h)
            preVal = h.val
            h = h.next
        if not headAry:
            return None
        return headAry[0]