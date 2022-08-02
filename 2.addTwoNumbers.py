import numpy as np
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def listNode2List(self, ln):
        l = [];
        n = ln;
        while n is not None:
            l.append(n.val);
            n = n.next;
        return self.arrayReverse(l);
    def list2ListNode(self,items):
        items = self.arrayReverse(items)
        n = ListNode(items[0]);
        rlt = n;
        for i in range(1, len(items)):
            n.next = ListNode(items[i]);
            n = n.next;
        return rlt;
    def arrayReverse(self,items):
        return list(np.flipud(items));
    def addTwoNumbers(self, l1, l2):
        l1 = self.listNode2List(l1);
        l2 = self.listNode2List(l2);
        aStrL1 = list(map(str,l1));#將 int array to string array
        aStrL2 = list(map(str,l2));
        sSingleL1 = ''.join(aStrL1);#將 string array to Single string
        sSingleL2 = ''.join(aStrL2);
        iSingleL1 = int(sSingleL1);#將 string to int
        iSingleL2 = int(sSingleL2);
        iRlt = iSingleL1 + iSingleL2;
        sRlt = str(iRlt);#轉 string
        aStrRlt = list(sRlt);#將 String 切成 char
        return self.list2ListNode((list(map(int,aStrRlt))));

ttt = Solution();
print( ttt.addTwoNumbers(ttt.list2ListNode([2,4,9]), ttt.list2ListNode([5,6,4,9])))