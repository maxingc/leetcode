# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            def traversal(left, right):
                if left > right:
                    return None
                val = postorder.pop()
                node = TreeNode(val)
                index = idx_map[val]
                node.right = traversal(index + 1, right)
                node.left = traversal(left, index - 1)
                return node

            idx_map = {val: index for index, val in enumerate(inorder)}
            return traversal(0, len(inorder) - 1)

    #my solution
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        head = TreeNode()
        queue = collections.deque()
        if postorder:
            head.val = postorder[-1]
            queue.append([inorder, postorder, head])
        while queue:
            cur = queue.pop()
            inorder = cur[0]
            postorder = cur[1]
            node = cur[2]
            for i in range(len(inorder)):
                if inorder[i] == postorder[-1]:
                    if i-1>=0:
                        left_node = TreeNode(postorder[i-1])
                        node.left = left_node
                        queue.append([inorder[:i], postorder[:i], left_node])
                    if len(postorder)-2>=i:
                        right_node = TreeNode(postorder[-2])
                        node.right = right_node
                        queue.append([inorder[i+1:], postorder[i:-1], right_node])
                    break
        return head