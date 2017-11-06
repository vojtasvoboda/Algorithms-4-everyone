class Stack(object):
    def __init__(self):
        self.stack_list = []

    def __len__(self):
        return len(self.stack_list)

    def __str__(self):
        return str(self.stack_list)

    def push(self, item):
        self.stack_list.append(item)
        return item

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def is_empty(self):
        return len(self) == 0

    def find(self, item):
        return self.stack_list.index(item)
