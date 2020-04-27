#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (41.06%)
# Likes:    475
# Dislikes: 0
# Total Accepted:    82.7K
# Total Submissions: 199K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # TODO: 1.中间折叠(翻转)
        if not head or not head.next:return True
        fast,slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow #if not fast.next,mid是正中间 else mid是mid_left
        right = slow.next
        while right:
            slow,right.next,right = right,slow,right.next
        p1,p2 = head,slow
        while p2!=mid:
            if p1.val!=p2.val:
                return False
            p1,p2 = p1.next,p2.next
        return True

        
        # TODO: 2.栈
        # TODO: 3.复制链表进数组
        # TODO: 4.递归
# @lc code=end

