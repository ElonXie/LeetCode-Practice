#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (59.62%)
# Likes:    239
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 37.3K
# Testcase Example:  '[5,2,13]'
#
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater
# Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
# 
# 
# 
# 例如：
# 
# 输入: 原始二叉搜索树:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# 输出: 转换为累加树:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
# 
# 
# 
# 
# 注意：本题和 1038:
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(root,sum):
            if not root:
                return 
            dfs(root.right,self.sum)
            root.val += self.sum
            self.sum = root.val
            dfs(root.left,self.sum)
        dfs(root,self.sum)
        return root
# @lc code=end

