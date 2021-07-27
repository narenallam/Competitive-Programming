class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, _data):
        self.stack.append(_data)

    def top(self):
        self.stack[-1]

    def empty(self):
        return False if self.stack else True

    def __str__(self):
        return str(self.stack)