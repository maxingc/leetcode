# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(root):
            if root == None:
                return
            root.left, root.right = root.right, root.left
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return root
