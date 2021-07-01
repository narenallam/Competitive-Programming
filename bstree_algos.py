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
    ...

def mirror_image(_root):
    ...

def hill_climb_traversal(_root):
    ...
    {
        1: [30],
        2: [15, 60],
        3: [7, 22, 45, 75],
        4: [17, 27]
    }

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

side_view()

