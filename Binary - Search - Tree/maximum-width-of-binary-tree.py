# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 
        queue = deque([(root , 0)])
        ans = 0
        while queue:
            size = len(queue)
            first = last = 0
            min_index = queue[0][1]
            for i in range(size):
                
                node , idx = queue.popleft()
                index = idx - min_index
                if i == 0:
                    first = index
                last = index
                if node.left:
                    queue.append((node.left , 2 * index))
                if node.right:
                    queue.append((node.right , 2* index +1))
                ans = max(ans , last- first +1)
        return ans
