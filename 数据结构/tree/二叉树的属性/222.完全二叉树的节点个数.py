# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        left_height = 0
        right_height = 0
        while left:
            left = left.left
            left_height += 1
        while right:
            right = right.right
            right_height += 1
        if left_height == right_height:
            return (2<<left_height) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1