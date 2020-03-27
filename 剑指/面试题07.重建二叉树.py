'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.dic = {}
        for i,v in enumerate(inorder):
            self.dic[v] = i
        self.recur(0,0,len(inorder)-1)
    
    def recur(rootIndex,left_in,right_in):
        if left_in>right_in:
            return None            
        root = TreeNode(self.preorder[rootIndex])
        i = self.dic[self.preorder[rootIndex]]
        root.left = self.recur(rootIndex+1,left_in,i-1)
        root.right = self.recur(rootIndex+1+i-left_in,i+1,right_in)
        return root
















class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.pre,self.dic = preorder,{}
        for i,v in enumerate(inorder):
            self.dic[v] = i
        return self.recur(0,0,len(inorder)-1)
    
    def recur(self,root,left_in,right_in):
        if left_in>right_in:
            return
        rootNode = TreeNode(self.pre[root])
        i = self.dic[self.pre[root]]
        rootNode.left = self.recur(root+1,left_in,i-1)
        rootNode.right = self.recur(root+i-left_in+1,i+1,right_in)
        return rootNode

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         left_pre,right_pre = 0,len(preorder)-1
#         left_in,right_in = left_pre,right_pre
#         return self.rebuildTree(preorder,inorder,left_pre,right_pre,left_in,right_in)


#     def rebuildTree(self,preorder,inorder,left_pre,right_pre,left_in,right_in):
#         root_val = preorder[left_pre]
#         root = TreeNode(root_val)

#         root_in_index = left_in
#         while(inorder[root_in_index]!=root_val):
#             root_in_index += 1
#         left_nums = root_in_index-left_in
#         right_nums = right_in-root_in_index
#         if left_nums:
#             root.left = self.rebuildTree(preorder,inorder,left_pre+1,left_pre+left_nums,left_in,root_in_index-1)
#         if right_nums:
#             root.right = self.rebuildTree(preorder,inorder,left_pre+1+left_nums,right_pre,root_in_index+1,right_in)

#         return root

    
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         self.dic, self.po = {}, preorder
#         for i in range(len(inorder)):
#             self.dic[inorder[i]] = i
#         return self.recur(0, 0, len(inorder) - 1)

#     def recur(self, pre_root, in_left, in_right):
#         if in_left > in_right: return # 终止条件：中序遍历为空
#         root = TreeNode(self.po[pre_root]) # 建立当前子树的根节点
#         i = self.dic[self.po[pre_root]]    # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
#         root.left = self.recur(pre_root + 1, in_left, i - 1) # 开启左子树的下层递归
#         root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right) # 开启右子树的下层递归
#         return root # 返回根节点，作为上层递归的左（右）子节点
        
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         self.dic = {}
#         self.pre = preorder
#         for i in range(len(inorder)):
#             self.dic[inorder[i]] = i
#         return self.recur(0,0,len(inorder)-1)
    
#     def recur(self, pre_root, in_left, in_right):
#         if in_left>in_right:
#             return
#         root = TreeNode(self.pre[pre_root])
#         i = self.dic[self.pre[pre_root]]
#         root.left = self.recur(pre_root+1, in_left, i-1)
#         root.right = self.recur(pre_root+i-in_left+1, i+1, in_right)
#         return root

if __name__ == '__main__':
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = s.buildTree(preorder,inorder)
    print(root)