#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (54.54%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    30.3K
# Total Submissions: 55.3K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 
# 找出路径和等于给定数值的路径总数。
# 
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
# 
# 示例：
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # countPath是从当前节点出发, pathSum是当前树中. 
    # 因此 pathSum(root) = countPath(root)+pathSum(root.left)+pathSum(root.right)
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        result = self.countPath(root,sum)
        a = self.pathSum(root.left,sum)
        b = self.pathSum(root.right,sum)
        return result+a+b

    def countPath(self,root,sum):
        if not root:
            return 0
        sum -= root.val
        result = 1 if not sum else 0
        result += self.countPath(root.left,sum)+self.countPath(root.right,sum)
        return result

            
        
# @lc code=end

def generateTree(tree_list):
    stack = []
    root = TreeNode(tree_list[0])
    stack.append(root)
    i = 0
    while len(stack):
        cur = stack.pop(0)
        if cur:
            if tree_list[i+1]:
                cur.left = TreeNode(tree_list[i+1])
            else:
                cur.left = None
            if tree_list[i+2]:
                cur.right = TreeNode(tree_list[i+2])
            else:
                cur.right = None
            stack.append(cur.left)
            stack.append(cur.right)
        else:
            stack.append(None)
            stack.append(None)
        i+=2
        if i >= len(tree_list):
            break
    return root

    
if __name__ == '__main__':
    s = Solution()
    tree_list =  [10,5,-3,3,2,None,11,3,-2,None,1]
    root = generateTree(tree_list)
    s.pathSum(root,8)