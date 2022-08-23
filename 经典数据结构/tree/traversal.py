
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    #层序遍历
    ##迭代法
    def levelOrder(self, root):
        results = []
        if not root:
            return results

        que = deque([root])

        while que:
            size=len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results

    ##递归法
    def levelOrder(self, root):
        res = []
        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)
        helper(root, 0)
        return res

    # 深度遍历
    # 递归遍历
    ##前序遍历
    def preorderTraversal(self, root):
        result = []

        def traversal(root):
            if root == None:
                return
            result.apend(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return result


    ##中序遍历
    def inorderTraversal(self, root):
        result = []

        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)

        traversal(root)
        return result


    ##后序遍历
    def postorderTraversal(self, root):
        result = []

        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        traversal(root)
        return result


    # 迭代遍历 v1
    ## 前序遍历
    def preorderTraversal(self, root):
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
                st.append(node)
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)

        return result


    def inorderTraversal(self, root):
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right:
                    st.append(node.right)
                st.append(node)
                st.append(None)
                if node.left:
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result


    def postorderTraversal(self, root):
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                st.append(node)
                st.append(None)
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result


    # 迭代遍历 v2
    ##前序遍历
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            ##中间节点先处理
            result.append(node.val)
            ##右子节点先入栈
            if node.right:
                stack.append(node.right)
            ##左子节点后入栈
            if node.left:
                stack.append(node.left)
        return result


    ##中序遍历 一直先访问左节点
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result


    ##后序遍历 中右左，之后再倒序返回
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]