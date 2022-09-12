# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, depth):
            if not root:
                return depth
            if not root.left and not root.right:
                return depth+1
            min_left = min_right = float("inf")
            if root.left:
                min_left = helper(root.left, depth+1)
            if root.right:
                min_right = helper(root.right, depth+1)
            return min(min_left, min_right)
        return helper(root, 0)