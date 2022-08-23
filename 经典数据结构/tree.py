class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #递归遍历
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

    #迭代遍历
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