# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None

        def inorder(root):

            if root is None or self.result is not None:
                return

            inorder(root.left)
            self.k -= 1

            if self.k == 0:
                self.result = root.val
            
            inorder(root.right)
        
        inorder(root)
        return self.result
""" 
        5
    3       6
   2 4
  1

inorder traversal
left
node  (process)
right
kth time processing 
"""