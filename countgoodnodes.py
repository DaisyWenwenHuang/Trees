# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# leetcode 1448 medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,maxval):
            if not root:
                return 0
            if root.val >= maxval:
                res = 1
            else:
                res = 0
            maxval = max(root.val,maxval)
            res += dfs(root.right,maxval)
            res += dfs(root.left,maxval)
            return res
        
        return dfs(root,root.val)
