# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def traversal(left, right):
            if left > right:
                return None

            val = preorder.popleft()
            node = TreeNode(val)
            index = idx_map[val]

            node.left = traversal(left, index - 1)
            node.right = traversal(index + 1, right)

            return node

        preorder = collections.deque(preorder)
        idx_map = {val: index for index, val in enumerate(inorder)}
        return traversal(0, len(inorder) - 1)