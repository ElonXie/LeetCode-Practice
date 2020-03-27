#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (59.90%)
# Likes:    878
# Dislikes: 0
# Total Accepted:    195.6K
# Total Submissions: 325.5K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ans = head
        while l1 and l2:
            if l1.val<= l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
            else:
                ans.next = ListNode(l2.val)
                ans, l2 = ans.next,l2.next
        while l1:
            ans.next =ListNode(l1.val)
            ans,l1 = ans.next,l1.next
        while l2:
            ans.next = ListNode(l2.val)
            ans,l2 = ans.next,l2.next
        return head.next

# @lc code=end

