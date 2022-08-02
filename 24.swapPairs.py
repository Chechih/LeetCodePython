from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return head
        headInd = []
        h = head
        while(h != None):
            headInd.append(h)
            h = h.next
        headIndCount = len(headInd)
        for i in range(0, headIndCount, 2):
            if(i + 1 < headIndCount):
                temp = headInd[i]
                headInd[i] = headInd[i + 1]
                headInd[i + 1] = temp
        
        for i in range(headIndCount):
            hi = headInd[i]
            if(i + 1 < headIndCount):
                hi.next = headInd[i + 1]
            else:
                hi.next = None

        return headInd[0]
        
aaa = ListNode(1)
tttt = Solution()
print(tttt.swapPairs(aaa))