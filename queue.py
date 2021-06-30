class Queue:
    def __init__(self):
        self.q = []

    def deque(self):
        return self.q.pop(0)

    def enque(self, _data):
        self.q.append(_data)

    def head(self):
        self.q[0]

    def tail(self):
        self.q[-1]

    def empty(self):
        return False if self.q else True

    def __str__(self):
        return str(self.q)