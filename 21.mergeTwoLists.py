from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if(l1 == None and l2 == None):
            return None
        elif(l1 == None):
            return l2
        elif(l2 == None):
            return l1
        newlist = None
        if(l1.val < l2.val):
            newlist = ListNode(l1.val)
            l1 = l1.next
        else:
            newlist = ListNode(l2.val)
            l2 = l2.next
        rlt = newlist
        while(l1 != None or l2 != None):
            if(l2 == None or (l1 != None and l1.val < l2.val)):
                newlist.next = ListNode(l1.val)
                l1 = l1.next
            else:
                newlist.next = ListNode(l2.val)
                l2 = l2.next
            newlist = newlist.next
        return rlt
            
aaa = ListNode(1, ListNode(2, ListNode(4)))
bbb = ListNode(1, ListNode(3, ListNode(4)))
tttt = Solution()
print(tttt.mergeTwoLists(aaa, bbb))
