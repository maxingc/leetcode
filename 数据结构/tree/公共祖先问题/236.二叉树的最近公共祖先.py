# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #        def dfs(node, p, q):
        #            if node is None:
        #                return False
        #            lson = dfs(node.left, p, q)
        #            rson = dfs(node.right, p, q)
        #            if (lson and rson) or ((lson or rson) and (p.val==node.val or q.val==node.val)):
        #                ans = node
        #            return lson or rson or p.val==node.val or q.val==node.val
        #
        ##        ans = TreeNode()
        #        dfs(root, p, q)
        #        return ans
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right