#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (50.57%)
# Likes:    735
# Dislikes: 0
# Total Accepted:    127.1K
# Total Submissions: 250.1K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root: TreeNode) -> bool:
        # TODO: 方法3 递归
        def isMirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val==t2.val and isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)
        return isMirror(root,root)



        # TODO: 方法2  方法1过不了测试(时间复杂度),因为每次是按层来处理.
        # 方法2, 每次把对称位置节点按"节点对"放入队列, 然后按节点对取出.
        # 解构了一整层求回文的需求
        # queue = [root,root]
        # while queue:
        #     p1,p2 = queue.pop(0),queue.pop(0)
        #     if not p1 and not p2:
        #         continue
        #     if not p1 or not p2:
        #         return False
        #     if not p1.val == p2.val:
        #         return False
        #     else:
        #         queue.append(p1.left)
        #         queue.append(p2.right)
        #         queue.append(p1.right)
        #         queue.append(p2.left)
        # return True
            

        # TODO: 方法1
        # stack1, stack2 = [],[]
        # stack1.append(root)
        # # 迭代方法

        # def symmetric(arr_to_do):
        #     n = len(arr_to_do)
        #     for i in range(n//2):
        #         if arr_to_do[i]!=arr_to_do[n-i-1]: return False
        #     return True
        # while stack1:
        #     # 当stack1全是None,结束
        #     flag = False
        #     for i in stack1:
        #         if not i==None: flag = True
        #     if not flag: break

        #     # 层序遍历树, stack2为当前要遍历的节点. stack1为下一层所有节点
        #     # arr_to_do为需要判断是否回文的数组
        #     stack2 = stack1
        #     stack1 = []
        #     arr_to_do = []
        #     while stack2:
        #         cur = stack2.pop(0)
        #         if not cur: 
        #             arr_to_do.append(None)
        #             stack1.append(None)
        #             stack1.append(None)
        #         else:
        #             arr_to_do.append(cur.val)
        #             stack1.append(cur.left)
        #             stack1.append(cur.right)
        #     if not symmetric(arr_to_do):
        #         return False
        # return True


            

# @lc code=end

