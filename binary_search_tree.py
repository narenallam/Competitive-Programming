from queue import Queue
from stack import Stack


class Node:
    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class BinarySearchTree:
    """
    L < P < R
    """
    def __init__(self, items):
        self.root = None
        self.count = 0
        self._depth = 0
        for item in items:
            self.insert(item)

    def insert(self, _data): # O(n)
        new_node = Node(_data)

        if self.root is None:
            self.root = new_node
        else:
            cur = self.root
            prev = None
            while cur:
                prev = cur
                if cur.data < new_node.data:
                    cur = cur.right
                else:
                    cur = cur.left

            if prev.data < new_node.data:
                prev.right = new_node
            else:
                prev.left = new_node

        self.count += 1

    def in_order(self, _root):
        if _root:
            self.in_order(_root.left)
            print(_root.data, end=" ")
            self.in_order(_root.right)

    def rev_in_order(self, _root):
        if _root:
            self.rev_in_order(_root.right)
            print(_root.data, end=" ")
            self.rev_in_order(_root.left)

    def pre_order(self, _root):
        if _root:
            print(_root.data, end=" ")
            self.pre_order(_root.left)
            self.pre_order(_root.right)

    def post_order(self, _root):
        if _root:
            self.post_order(_root.left)
            self.post_order(_root.right)
            print(_root.data, end=" ")

    def level_order(self):
        _root = self.root
        if _root:
            q = Queue()
            q.enque(_root)
            while not q.empty():
                # print(q)
                node = q.deque()
                print(node.data, end=" ")
                if node.left:
                    q.enque(node.left)
                if node.right:
                    q.enque(node.right)

    def depth(self):
        def go_deep(_root, level):
            if _root:
                if self._depth < level:
                    self._depth = level
                go_deep(_root.left, level + 1)
                go_deep(_root.right, level + 1)

        go_deep(self.root, 1)
        return self._depth

    def in_order_nr(self):
        current = self.root
        stack = Stack()

        while True:
            if current is not None:
                stack.push(current)
                current = current.left

            elif not stack.empty():
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right

            else:
                break

    def pre_order_nr(self):
        if self.root is None:
            return

        stack = Stack()
        stack.push(self.root)

        while not stack.empty():

            node = stack.pop()
            print(node.data, end=" ")

            if node.left is not None:
                stack.push(node.left)

            if node.right is not None:
                stack.push(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree([30, 15, 60, 7, 22, 45, 75, 17, 27])
    # bst.in_order(bst.root)
    bst.in_order_nr()
    bst.insert(50)
    print()
    bst.level_order()
    print("Depth:", bst.depth())