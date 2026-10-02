# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if not root:
            return 0
        return (
            self.findPath(root,targetSum)
            + self.pathSum(root.left,targetSum)
            + self.pathSum(root.right,targetSum)
        )
    def findPath(self,root,targetSum):
        if not root:
            return 0
        count = 0
        if root.val == targetSum:
            count += 1
        count += self.findPath(root.left,targetSum - root.val)
        count += self.findPath(root.right,targetSum - root.val)
        return count
