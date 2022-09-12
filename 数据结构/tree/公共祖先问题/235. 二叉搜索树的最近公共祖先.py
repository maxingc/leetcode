# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node == None:
                return None
            if node.val >= min_value and node.val <= max_value:
                return node
            elif node.val < min_value:
                return helper(node.right)
            else:
                return helper(node.left)

        min_value = min(p.val, q.val)
        max_value = max(p.val, q.val)

        return helper(root)

