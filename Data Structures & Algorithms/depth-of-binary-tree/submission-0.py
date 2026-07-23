# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
        	return 0
        return 1 + self.helper(root)


    def helper(self, root):
    	if not root.left and not root.right:
    		return 0
    	if root.left and root.right:
    		return max(self.helper(root.left), self.helper(root.right)) + 1
    	if root.left:
    		return self.helper(root.left) + 1
    	if root.right:
    		return self.helper(root.right) + 1