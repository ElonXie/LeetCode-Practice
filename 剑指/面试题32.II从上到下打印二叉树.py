# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack1,stack2 = [],[]
        stack = []
        stack1.append(root)
        while stack1 or stack2:
            if not stack1:
                stack.append([])
                while stack2:                    
                    curP = stack2.pop(0)
                    if curP:
                        stack[-1].append(curP.val)
                    if curP.left:
                        stack1.append(curP.left)
                    if curP.right:
                        stack1.append(curP.right)
            if not stack2:
                stack.append([])
                while stack1:
                    curP = stack1.pop(0)
                    if curP:
                        stack[-1].append(curP.val)
                    if curP.left:
                        stack2.append(curP.left)
                    if curP.right:
                        stack2.append(curP.right)
        return stack
