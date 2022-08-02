from typing import List
from typing import Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listsCount = len(lists)
        if(listsCount < 1):
            return None
        allItems = []
        for l in lists:
            nowInd = l
            while(nowInd != None):
                allItems.append(nowInd.val)
                nowInd = nowInd.next
        allItems.sort()
        rlt = None
        allItemsCount = len(allItems)
        if(allItemsCount > 0):
            rlt = ListNode(allItems[0])
        allItems = allItems[1:allItemsCount]
        allItemsCount = len(allItems)
        nowTarget = rlt
        for ai in allItems:
            nowTarget.next = ListNode(ai)
            nowTarget = nowTarget.next

        return rlt

aaa = []
for k in range(10000):
    aaa.append(ListNode(random.randint(0,99)))

tttt = Solution()
print(tttt.mergeKLists(aaa))
        
        