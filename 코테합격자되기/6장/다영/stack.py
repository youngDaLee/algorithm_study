"""
스택 구현하기
"""

class stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data);

    def top(self):
        return self.stack[-1]
