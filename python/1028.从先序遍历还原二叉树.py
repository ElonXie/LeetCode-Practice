#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
#
# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (61.05%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 6.1K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# 我们从二叉树的根节点 root 开始进行深度优先搜索。
# 
# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D +
# 1。根节点的深度为 0）。
# 
# 如果节点只有一个子节点，那么保证该子节点为左子节点。
# 
# 给出遍历输出 S，还原树并返回其根节点 root。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入："1-2--3--4-5--6--7"
# 输出：[1,2,5,3,4,6,7]
# 
# 
# 示例 2：
# 
# 
# 
# 输入："1-2--3---4-5--6---7"
# 输出：[1,2,5,3,null,6,null,4,null,7]
# 
# 
# 示例 3：
# 
# 
# 
# 输入："1-401--349---90--88"
# 输出：[1,401,null,349,88,90]
# 
# 
# 
# 
# 提示：
# 
# 
# 原始树中的节点数介于 1 和 1000 之间。
# 每个节点的值介于 1 和 10 ^ 9 之间。
# 
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
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 1. 首先考虑用栈存储历史节点
        # 根据新节点和上一次节点的深度差值,判断是否需要pop
        # 2. 后边改用列表,每个深度只存储一个,因为一个子节点必左
        if not S: return None
        nodes = []
        cur_point,cur_num = 0,0
        old_level = 0
        while cur_point < len(S):
            point = cur_point
            while S[point]=='-': point+=1
            cur_num, level = point, point-cur_point
            while point<len(S) and S[point]!='-': point+=1
            value = int(S[cur_num:point])
            cur_point = point
            if level==0: nodes.append(TreeNode(value))
            elif level<len(nodes):
                if level<=old_level:
                    nodes[level] = TreeNode(value)
                    nodes[level-1].right = nodes[level]
                else:
                    nodes[level] = TreeNode(value)
                    nodes[old_level].left = nodes[level]
            else:
                nodes.append(TreeNode(value))
                nodes[level-1].left = nodes[level]
            old_level = level
        return nodes[0]
                
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.recoverFromPreorder('1-2-3--4')