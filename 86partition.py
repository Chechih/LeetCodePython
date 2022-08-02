from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def list2ListNode(items):
        n = ListNode(items[0]);
        rlt = n;
        for i in range(1, len(items)):
            n.next = ListNode(items[i]);
            n = n.next;
        return rlt;
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = []
        greaterEqual = []
        h = head
        while h is not None:
            val = h.val
            if val >= x :
                greaterEqual.append(h)
            else:
                less.append(h)
            h = h.next
        firstH = None
        if len(less) > 0:
            firstH = less[0]
        elif len(greaterEqual) > 0:
            firstH = greaterEqual[0]
        allHeadAry = less + greaterEqual

        for i in range(len(allHeadAry) - 1):
            h = allHeadAry[i]
            h.next = allHeadAry[i + 1]
        if len(allHeadAry) > 0:
            h = allHeadAry[-1]
            h.next = None

        return firstH

tttt = Solution()
print(tttt.partition(
    ListNode.list2ListNode(
[2,1,3]), 2
))