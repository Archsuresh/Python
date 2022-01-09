class Stack():
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def isempty(self):
        return self.items==[]

    def peek(self):
        if not self.isempty():
            return self.items[-1]

"""
s=Stack()

s.push('a')
s.push('b')
s.push('c')
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.isempty())
print(s.peek())

"""
