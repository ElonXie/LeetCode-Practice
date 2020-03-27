# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # sum -= cur.val  + 递归
        if not root:
            return []
        path = []
        ans = []
        def dfs(node,path,cur_sum):
            cur_sum -= node.val
            if not node.left and not node.right and not cur_sum:
                ans.append(path+[node.val])
            if node.left:
                dfs(node.left,path+[node.val],cur_sum)
            if node.right:
                dfs(node.right,path+[node.val],cur_sum)
        dfs(root,path,sum)
        return ans
            

                