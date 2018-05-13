class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)

old_list = [1, 2, 3, 4, 5]
new_list = []
stack = Stack()
for i in old_list:
    stack.push(i)

for i in range(len(stack.items)):
    new_list.append(stack.pop())

print(new_list)