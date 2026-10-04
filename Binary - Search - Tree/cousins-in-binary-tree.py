# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        if not root:
            return False
        queue = deque([root])
        while queue:
            foundx = False
            foundy = False
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.val == x:
                    foundx = True
                if node.val == y:
                    foundy = True
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y or node.left.val ==y and node.right.val == x:
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if foundx and foundy:
                return True
            if foundx or foundy:
                return False
        return False
