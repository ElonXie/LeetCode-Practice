#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode-cn.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (75.44%)
# Likes:    349
# Dislikes: 0
# Total Accepted:    45.3K
# Total Submissions: 59.7K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
# 
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL
# 的节点将直接作为新二叉树的节点。
# 
# 示例 1:
# 
# 
# 输入: 
# Tree 1                     Tree 2                  
# ⁠         1                         2                             
# ⁠        / \                       / \                            
# ⁠       3   2                     1   3                        
# ⁠      /                           \   \                      
# ⁠     5                             4   7                  
# 输出: 
# 合并后的树:
# 3
# / \
# 4   5
# / \   \ 
# 5   4   7
# 
# 
# 注意: 合并必须从两个树的根节点开始。
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(t1,t2):
            if not t1 and not t2:
                return None
            if not t1:
                t1 = TreeNode(t2.val)
            elif t2:
                t1.val = t1.val+t2.val
            if t2:
                t1.left = dfs(t1.left,t2.left)
                t1.right = dfs(t1.right,t2.right)
            if not t2:
                t1.left = dfs(t1.left,None)
                t1.right = dfs(t1.right,None)
            return t1
        root = dfs(t1,t2)
        return root
# @lc code=end

