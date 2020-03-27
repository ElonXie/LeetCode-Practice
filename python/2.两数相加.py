#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (36.72%)
# Likes:    3994
# Dislikes: 0
# Total Accepted:    344.2K
# Total Submissions: 935.4K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans_head = ListNode(0)        
        ans = ans_head
        d = 0
        while l1 and l2:
            res = l1.val+l2.val+d
            if res>9:
                res -= 10
                d = 1
            else:
                d = 0
            l1 = l1.next
            l2 = l2.next
            ans.next = ListNode(res)
            ans = ans.next
        while l1:
            res = l1.val+d
            if res==10:
                res = 0
                d = 1
            else:
                d = 0
            l1 = l1.next
            ans.next = ListNode(res)
            ans = ans.next
        while l2:
            res = l2.val+d
            if res==10:
                res = 0
                d = 1
            else:
                d = 0
            l2 = l2.next
            ans.next = ListNode(res)
            ans = ans.next
        ans.next = None if not d else ListNode(d)
        if ans.next:
            ans.next.next = None
        return ans_head.next
# @lc code=end

