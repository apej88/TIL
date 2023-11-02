class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def __len__(self):
        return self.length
        
    def push(self, data):
        node = Node(data)
        
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        
        self.length += 1
    
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
        link = link.next
        
        while(True):
            if(link is None) : break
            res += "," + str(link.data)
            link = link.next
        
        res += " ]" 
        return res       