from c_stack import Stack
from b_hashtable import HashTable

def is_pair(text):
    hashtable = HashTable()
    hashtable.add('(',')')
    hashtable.add('[',']')
    hashtable.add('{','}')
    
    stack = Stack()
    
    for ch in text:
        if ch in hashtable:
            stack.push(ch)
            continue
        
        if stack.is_empty() : return False
        k = stack.pop()
        
        if ch != hashtable.get(k):
            return False
    
    return True if stack.is_empty() else False
    
   

