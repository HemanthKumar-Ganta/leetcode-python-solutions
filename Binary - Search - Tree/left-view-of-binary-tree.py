''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def leftView(self, root):
        # code here
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    ans.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return ans
