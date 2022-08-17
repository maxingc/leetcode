class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self._head, self._tail = Node(0), Node(0) #虚拟节点
        self._head.next, self._tail.prev = self._tail, self._head
        self._count = 0

    def _get_node(self, index):
        if index >= self._count // 2:
            node = self._tail
            for _ in range(self._count - index):
                node = node.prev
        else:
            node = self._head
            for _ in range(index+1):
                node = node.next
        return node

    def _update(self, prev, next, val):
        self._count += 1
        node = Node(val)
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            node = self._get_node(index)
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self._update(self._head, self._head.next, val)

    def addAtTail(self, val: int) -> None:
        self._update(self._tail.prev, self._tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._count:
            return
        node = self._get_node(index)
        self._update(node.prev, node, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            node = self._get_node(index)
            self._count -= 1
            node.prev.next, node.next.prev = node.next, node.prev
