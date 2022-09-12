# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        head = TreeNode(val=float('inf'), left=root)
        node = head
        while True:
            if node.val < key:
                if not node.right:
                    return head.left
                if node.right.val == key:
                    if node.right.left is None or node.right.right is None:
                        node.right = node.right.left if node.right.left else node.right.right
                        return head.left
                    left = node.right.left
                    node.right = node.right.right
                    node = node.right
                    while node.left:
                        node = node.left
                    node.left = left
                    return head.left
                node = node.right
            else:
                if not node.left:
                    return head.left
                if node.left.val == key:
                    if node.left.left is None or node.left.right is None:
                        node.left = node.left.left if node.left.left else node.left.right
                        return head.left
                    left = node.left.left
                    node.left = node.left.right
                    node = node.left
                    while node.left:
                        node = node.left
                    node.left = left
                    return head.left
                node = node.left


