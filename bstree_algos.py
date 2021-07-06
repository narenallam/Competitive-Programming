from binary_search_tree import BinarySearchTree
from queue import Queue

def side_view():
    level_completed = set()
    def pre_order(_root, level):
        if _root:
            if level not in level_completed:
                print(_root.data, end=" ")
                level_completed.add(level)

            pre_order(_root.left, level + 1)
            pre_order(_root.right, level + 1)

    bst = BinarySearchTree([30, 15, 60, 22, 45, 75, 17, 27])
    pre_order(bst.root, 1)

def replace_node_with_sum_of_the_child():
    #bst = BinarySearchTree([4, 2, 6, 3, 1, 5, 7])
    bst = BinarySearchTree([1, 2, 3, 4, 5, 6, 7])

    def replace_me(_root):
        if _root:
            bak = _root.data
            _root.data = replace_me(_root.left) + replace_me(_root.right)
            return bak

        return 0

    replace_me(bst.root)
    level_order(bst.root)


def mirror_image():
    bst = BinarySearchTree([4, 2, 6, 3, 1, 5, 7])
    def swap_child(_root):
        if _root:
            swap_child(_root.left)
            swap_child(_root.right)
            _root.left, _root.right = _root.right, _root.left


    swap_child(bst.root)
    level_order(bst.root)

def hill_climb_traversal(_root):
    ...
    {
        1: [30],
        2: [15, 60],
        3: [7, 22, 45, 75],
        4: [17, 27]
    }

def level_order(_root):

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

mirror_image()

