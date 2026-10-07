# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        nodes =[]
        queue = deque([(root,0,0)])
        while queue:
            node,row,col = queue.popleft()
            nodes.append((col,row,node.val))
            if node.left:
                queue.append((node.left,row+1,col-1))
            if node.right:
                queue.append((node.right,row+1,col+1))
        nodes.sort()
        ans = []
        s = float("-inf")
        for col,row,value in nodes:
            if col != s:
                ans.append([])
                s = col
            ans[-1].append(value)
        return ans
