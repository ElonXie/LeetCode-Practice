#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (39.72%)
# Likes:    515
# Dislikes: 0
# Total Accepted:    47.2K
# Total Submissions: 113.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出: 6
# 
# 
# 示例 2:
# 
# 输入: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出: 42
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
    def maxPathSum(self, root: TreeNode) -> int:
        # 06.21:思路有,但是遍历树的方式已经忘了...
        self.max_sum = -float('inf')
        def maxGain(node):
            if not node:
                return 0
            left_gain = max(maxGain(node.left),0)
            right_gain = max(maxGain(node.right),0)
            cur_gain = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum,cur_gain)
            return node.val+max(left_gain,right_gain)
        maxGain(root)
        return self.max_sum
# @lc code=end

