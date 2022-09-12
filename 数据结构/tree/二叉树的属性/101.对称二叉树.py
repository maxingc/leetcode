# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## 递归
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traversal(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and traversal(p.left, q.right) and traversal(p.right, q.left)

        return traversal(root, root)

    ## 迭代
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        st = []
        if root:
            st.append(root)
            st.append(root)
        while st:
            p = st.pop()
            q = st.pop()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            st.append(p.left)
            st.append(q.right)
            st.append(p.right)
            st.append(q.left)
        return True

            ## my solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traversal(root, direction, depth):
            if root is None:
                return [None]
            if direction == 'left':
                    left_list = traversal(root.left, 'left', depth+1)
                    right_list = traversal(root.right, 'right', depth+1)
            else:
                    left_list = traversal(root.right, 'right', depth+1)
                    right_list = traversal(root.left, 'left', depth+1)
            if depth==0:
                if operator.eq(left_list, right_list):
                    return ['true']
                else:
                    return ['false']
            else:
                return [root.val] + left_list + right_list

        res = traversal(root, 'left', 0)
        if res[0]=='true':
            return True
        else:
            return False

