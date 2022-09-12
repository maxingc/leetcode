# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, minimum, maximum):
            if node is None:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            return helper(node.left, minimum, node.val) and helper(node.right, node.val, maximum)

        return helper(root, float('-inf'), float('inf'))

    ##中序遍历，单调队列
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = []
        order_list = []
        if root:
            stack.append(root)

        while stack:
            node = stack.pop()
            if node != None:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                if order_list and node.val <= order_list[-1]:
                    return False
                order_list.append(node.val)
        return True