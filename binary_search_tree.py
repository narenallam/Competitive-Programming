class Node:
    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, items=[]):
        self.root = None
        self.count = 0
        for item in items:
            self.insert(item)

    def insert(self, _data):
        new_node = Node(_data)

        if self.root is None:
            self.root = new_node
        else:
            cur = self.root
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

    def inorder(self, _root):
        if _root:
            self.inorder(_root.left)
            print(_root.data, end=" ")
            self.inorder(_root.right)


if __name__ == '__main__':
    bst = BinarySearchTree([30, 15, 60, 7, 22, 45, 75, 17, 27])
    bst.inorder(bst.root)