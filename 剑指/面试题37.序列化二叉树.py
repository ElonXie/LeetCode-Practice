# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[None]"
        ans = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(0)
            if node:
                stack.append(node.left)
                stack.append(node.right)
                ans.append(node.val)
            else:
                ans.append(None)
        ans = ','.join([str(num) for num in ans])
        return ans.strip(',None').replace('None','null')

            

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        data = [int(num) if num!='null' else None for num in data]
        stack = []
        stack.append(TreeNode(data.pop(0)))
        root = stack[0]
        while data:
            node = stack.pop(0)
            if not node:
                continue
            leftnode = TreeNode(data.pop(0))
            rightnode = TreeNode(data.pop(0))
            node.left = leftnode
            node.right = rightnode
            stack.append(leftnode)
            stack.append(rightnode)
        return root
            

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))