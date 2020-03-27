# Definition for a Node.
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:return 
        p=head
        while p:
            copy=Node(p.val)
            copy.next,p.next=p.next,copy
            p=copy.next
        
        p=head
        while p:
            next_org=p.next.next
            p.next.next=next_org.next if next_org else None
            p.next.random=p.random.next if p.random else None
            p=next_org
        return head.next
        





class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
import copy
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node = head
        if not node:
            return None
        while node:
            copy_node = copy.copy(node)
            copy_node.next = node.next
            node.next = copy_node
            node = copy_node.next
        node = head.next
        while node:
            if node.random:
                node.random = node.random.next
            if not node.next:
                break
            node = node.next.next
        node = head
        copy_head = head.next
        copy_node = copy_head
        while node:
            node.next = copy_node.next
            if copy_node.next:
                copy_node.next = node.next.next
            else:
                break
            node = node.next
            copy_node = node.next
        return copy_head

if __name__ == '__main__':
    s = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.random = head
    s.copyRandomList(head)