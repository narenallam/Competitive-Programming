class SimpleQueue:
    def __init__(self):
        self.q = []

    def deque(self):
        return self.q.pop(0)

    def exists(self, val):
        return val in self.q

    def enque(self, _data):
        self.q.append(_data)

    def head(self):
        self.q[0]

    def tail(self):
        self.q[-1]

    def empty(self):
        return False if self.q else True

    def clear(self):
        self.q.clear()

    def __str__(self):
        return str(self.q)