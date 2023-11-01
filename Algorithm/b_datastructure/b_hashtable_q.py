from b_hashtable import HashTable

def q1(text:str):
    hashtable = HashTable()
    
    for ch in text:
        if ch not in hashtable:
            hashtable.add(ch,1)
        else:
            hashtable.set(ch, hashtable.get(ch)+1)
    
    res = []
    max = 1
    
    for e in hashtable:
        if max < e.data : max = e.data
    
    for e in hashtable:
        if max == e.data : res.append(e.key)    
    
    return res