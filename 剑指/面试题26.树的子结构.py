
'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        pA,pB = A,B
        stack = []
        while(pA):
            if self.decisionCur(pA,pB):
                return True
            else:
                if pA.left:
                    stack.append(pA.left)
                if pA.right:
                    stack.append(pA.right)
                if stack:
                    pA = stack.pop(0)
                else:
                    return False  

    def decisionCur(self,nodeA,nodeB):
        if not nodeB:
            return True
        if not nodeA:
            return False
        ans = nodeA.val==nodeB.val
        ans = ans and self.decisionCur(nodeA.left,nodeB.left) and self.decisionCur(nodeA.right,nodeB.right)
        return ans
    
if __name__ == '__main__':
    s = Solution()
    A = TreeNode(3)
    A.left = TreeNode(5)
    A.right = TreeNode(0)
    A.left.left = TreeNode(3)
    A.left.right = TreeNode(4)
    B = TreeNode(1)
    B.left = TreeNode(-4)
    B.right = TreeNode(2)
    B.left.left = TreeNode(-1)
    B.left.right = TreeNode(3)
    B.right.left = TreeNode(-3)
    B.right.right = TreeNode(-4)
    B.left.left.left = TreeNode(0)
    B.left.left.right = TreeNode(-3)
    B.left.right.left = TreeNode(-1)
    # A = TreeNode(1)
    # A.left = TreeNode(2)
    # A.right = TreeNode(3)
    # A.left.left = TreeNode(4)
    # B = TreeNode(3)
    print(s.isSubStructure(A,B))