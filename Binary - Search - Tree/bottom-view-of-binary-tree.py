'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        s = {}
        queue = deque([(root,0)])
        while queue:
            node,col = queue.popleft()
            s[col] = node.data
                
            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
        return [s[key] for key in sorted(s)]
