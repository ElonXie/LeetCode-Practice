#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (63.94%)
# Likes:    430
# Dislikes: 0
# Total Accepted:    44K
# Total Submissions: 68.7K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        inA = head
        while inA:
            length += 1
            inA = inA.next
        if length<2:
            return
        step = 1
        while step<length:            
            L = head
            M,R = L
            for i in range(step):
                if M:
                    M = L.next
            if M:
                for i in range(step):
                    if R:
                        R = M.next
            inA,outLast = self.sortNodes(L,M,R)
            for i in range(length//step-1):
                L = outLast.next
                M,R = L
                for i in range(step):
                    if M:
                        M = L.next
                if M:
                    for i in range(step):
                        if R:
                            R = M.next
                inB,outB = self.sortNodes(L,M,R)
                outLast.next = inB
                outLast = outB
            step *= 2
        return head


    def sortNodes(self,L,M,R):
        if not M:
            return L,None
        headAns = ListNode(0)
        ans = headAns
        headL,headM = L,M
        while(L!=headM and M!=R):
            if L.val<=M.val:
                ans.next = L
                if L.next == headM:
                    outLast = L
                ans,L = ans.next,L.next
            else:
                ans.next = M
                if M.next == R:
                    outLast = R
                ans,M = ans.next,M.next
        while(L!=headM):
            ans.next = L
            if L.next == headM:
                outLast = L
            ans,L = ans.next,L.next
        while(M!=R):
            ans.next = M
            if M.next == R:
                outLast = R            
            ans,M = ans.next,M.next
        return headAns.next,outLast
            
# @lc code=end

if __name__ == "__":
    a = ListNode(4)
    a.next = ListNode(2)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(3)

    s = Solution()
    s.sortList(a)
    
