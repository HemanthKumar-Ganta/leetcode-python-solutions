# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(root,target,path):

            if not root:
                return []
            path.append(root.val)
        
            if not root.left and not root.right and root.val == target:
                ans.append(path[:])
            
            dfs(root.left,target - root.val,path)
            dfs(root.right,target - root.val,path)
            path.pop()
        dfs(root,targetSum,[])
        return ans
