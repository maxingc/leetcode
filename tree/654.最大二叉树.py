# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    ##单调栈
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
            queue = []
            cur = 0
            for x in nums:
                node = TreeNode(x)
                while queue and queue[-1].val < x:
                    node.left = queue.pop()
                if queue:
                    queue[-1].right = node
                queue.append(node)
            return queue[0]

    ##递归
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def traversal(left, right):
            if left >= right:
                return None
            max_val = float('-inf')
            max_pos = -1
            for i in range(left, right):
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_pos = i
            if max_pos == -1:
                return None

            node = TreeNode(max_val)
            node.left = traversal(left, max_pos)
            node.right = traversal(max_pos + 1, right)
            return node

        return traversal(0, len(nums))