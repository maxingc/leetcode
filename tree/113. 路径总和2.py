# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def travelsal(node, path, target):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None and node.val==target:
                ans.append(path)
            nxt_path = path.copy()
            travelsal(node.left, nxt_path, target-node.val)
            nxt_path = path.copy()
            travelsal(node.right, nxt_path, target-node.val)
        ans = []
        travelsal(root, [], targetSum)
        return ans

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
            def travelsal(node, path, target):
                if node is None:
                    return
                path.append(node.val)
                if node.left is None and node.right is None and node.val == target:
                    ans.append(path.copy())
                travelsal(node.left, path, target - node.val)
                travelsal(node.right, path, target - node.val)
                path.pop()

            ans = []
            travelsal(root, [], targetSum)
            return ans