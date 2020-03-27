
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def dfs(node,last_max = None):
            if not node.left and not node.right and not last_max:
                last_max = node
                self.first = node
                return last_max
            if node.left:
                last_max = dfs(node.left,last_max)
            if last_max:
                node.left = last_max
                last_max.right = node
                last_max = last_max.right
            if not last_max:
                last_max = node
                self.first = node
            ###########  这里很关键,有可能没有左叶节点.这时候第一个if语句恒不成立.需要用第三个if语句把这个节点给做成第一个
            if node.right:
                last_max = dfs(node.right,last_max)
            return last_max
        if not root:
            return None
        self.first = None
        self.last = dfs(root)
        self.first.left = self.last
        self.last.right = self.first

        return self.first

if __name__ == '__main__':
    s = Solution()
    root = Node(4)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(5)
    root = s.treeToDoublyList(root)
    print(root.right.val)