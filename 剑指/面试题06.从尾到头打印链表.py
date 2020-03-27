'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

'''
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def reversePrint(self, head: ListNode) -> List[int]:
    #     cur = head
    #     ans = []
    #     if not cur:
    #         return []
    #     left = None
    #     while cur:
    #         left,left.next,cur = cur,left,cur.next
    #     head = left
    #     while(left):
    #         ans.append(left.val)
    #         left = left.next
    #     return ans
    # def reversePrint(self, head: ListNode) -> List[int]:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        cur = head
        while cur:
            ans.append(cur.val)
            cur = cur.next
        return ans.reverse()

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    print(s.reversePrint(head))