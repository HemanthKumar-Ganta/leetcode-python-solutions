'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        if not root:
            return []
        s = {}
        queue = deque([(root,0)])
        while queue:
            node,col = queue.popleft()
            if col not in s:
                s[col] = node.data
            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
        return [s[key] for key in sorted(s)]
