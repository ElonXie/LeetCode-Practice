# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


### 这段代码很奇怪的是为什么执行结束会改变 l1
import copy
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        p1,p2 = l1,l2
        # if not p1 and not p2:
        #     return
        # if not p1:
        #     return p2
        # if not p2:
        #     return p1
        dHead = ListNode(-5)
        pd = dHead
        while(p1 and p2):
            if p1.val<p2.val:
                pd.next = p1
                pd = pd.next
                p1 = p1.next
            else:
                pd.next = p2
                pd = pd.next
                p2 = p2.next
        while(p1):
            pd.next = p1
            pd = pd.next
            p1 = p1.next
        while(p2):
            pd.next = p2
            pd = pd.next
            p2 = p2.next
        return dHead.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(0)
    l1.next =  ListNode(2)
    l2 = ListNode(0)
    # print(s.mergeTwoLists(l2,l1).val)
    l3 = s.mergeTwoLists(l1,l2)
    print(l3.val)
    print(s.mergeTwoLists(l1,l2).next.next.val)