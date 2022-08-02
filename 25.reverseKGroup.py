from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head == None):
            return None
        allItems = []
        #先把所有資料組成 array
        nowInd = head
        while(nowInd != None):
            allItems.append(nowInd.val)
            nowInd = nowInd.next
        allItemsCount = len(allItems)
        allItemsReversed = []
        previousval = -1
        for i in range(k, allItemsCount, k):
            previousval +=1
            allItemsReversed += reversed(allItems[previousval:i])#取出特定範圍的陣列反轉
            previousval = i - 1
        if(len(allItems[previousval + 1:allItemsCount]) == k):#如果還可以轉再轉一次
            allItemsReversed += reversed(allItems[previousval + 1:allItemsCount])
        else:
            allItemsReversed += allItems[previousval + 1:allItemsCount]
        allItems = allItemsReversed
        #往下次組回練表
        rlt = None
        if(allItemsCount > 0):
            rlt = ListNode(allItems[0])
        allItems = allItems[1:allItemsCount]
        allItemsCount = len(allItems)
        nowTarget = rlt
        for ai in allItems:
            nowTarget.next = ListNode(ai)
            nowTarget = nowTarget.next
        return rlt

aaa = ListNode(1, ListNode(2))
tttt = Solution()
print(tttt.reverseKGroup(aaa, 2))