#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.05%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    80.3K
# Total Submissions: 163.2K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ansHead = ListNode(0)
        ans = ansHead
        curMins = []
        for i in range(len(lists)-1,-1,-1):
            if not lists[i]:
                lists.pop(i)
        for i in range(len(lists)):
            curMins.append(lists[i].val)
        while curMins:
            minIndex, min = self.getMinIndex(curMins)#这里如果用优先队列,就更快
            ans.next = ListNode(min)
            ans = ans.next
            if lists[minIndex].next:
                lists[minIndex] = lists[minIndex].next
                curMins[minIndex] = lists[minIndex].val
            else:
                lists.pop(minIndex)
                curMins.pop(minIndex)
        return ansHead.next

    def getMinIndex(self,arr):
        if arr:
            min = arr[0]
            index = 0
            for i,num in enumerate(arr):
                if num<min:
                    min = num
                    index = i
            return index,min
# @lc code=end

if __name__=='__main__':
    # headA = ListNode(1)
    # headA.next = ListNode(4)
    # headA.next.next = ListNode(5)

    # headB = ListNode(1)
    # headB.next = ListNode(3)
    # headB.next.next = ListNode(4)

    # headC = ListNode(2)
    # headC.next = ListNode(6)

    # lists = [headA, headB, headC]

    lists = [[],[]]
    s = Solution()
    s.mergeKLists(lists)