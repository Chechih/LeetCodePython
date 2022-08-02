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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        scope = []
        h = head
        i = 1
        while h is not None:
            if i >= left and i <= right:
                scope.append(h)
            h = h.next
            i +=1
        reverseScopeVal = [r.val for r in scope[::-1]]
        for i, s in enumerate(scope):
            s.val = reverseScopeVal[i]

        return head if not head in scope else scope[0]


tttt = Solution()
print(tttt.reverseBetween(
    ListNode.list2ListNode(
[1,2,3,4,5]), 2, 4
))