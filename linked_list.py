class Node:
    def __init__(self, _data, _next=None):
        self.data = _data
        self.next = _next


class LinkedList:
    def __init__(self, _items=[]):
        self.head = None
        self.tail = None
        self.count = 0

        for item in _items:
            self.append(item)

    def append(self, _data):
        new_node = Node(_data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def insert(self, _data, pos):
        pass

    def pop(self, pos=None):
        pass

    def remove(self, _data):
        pass

    def __str__(self):
        _head = self.head
        s = "head -> "

        while _head:
            s += str(_head.data) + " -> "
            _head = _head.next

        s += "None"
        return s

    def __repr__(self):
        _head = self.head
        l = []
        while _head:
            l.append(str(_head.data))
            _head = _head.next

        return f"LinkedList([{', '.join(l)}])"


if __name__ == '__main__':
    ll = LinkedList([5, 6, 2, 4, 8, 1, 9])
    print(ll)