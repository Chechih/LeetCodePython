from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Optional 意思是可以是 None
        '''
        headInd = []
        h = head
        while(h != None):
            headInd.append(h)
            h = h.next
        headIndCount = len(headInd)
        target = headIndCount - n
        rlt = head
        if(target - 1 < 0):#如果沒有前一個節點
            if(target == 0):#且那個節點就是自己
                rlt = headInd[0].next
            else:
                rlt = None
        elif(target != headIndCount -1):
            headInd[target - 1].next = headInd[target + 1]
        else: 
            headInd[target - 1].next = None
        return rlt

tttt = Solution()
aaa = ListNode(1, ListNode(2))
print(tttt.removeNthFromEnd(aaa, 2))