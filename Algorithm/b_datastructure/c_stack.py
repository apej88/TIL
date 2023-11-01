class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.top = None

class Stack:
    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None : return None
        res = self.top.data
        self.top = self.top.next
        return res

    def peek(self):
        if self.top is None : return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def __str__(self):
        if self.top is None : return "[]"
        
        link = self.top
        res = "[ " + str(link.data)
        while True:
            if link.next is None: break
            res += ", " + str(link.data)
            link = link.next
        
        res += " ]"
        return res