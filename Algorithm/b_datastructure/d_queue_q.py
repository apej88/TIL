from d_queue import Queue

def q1(n):
    queue = Queue()
    
    for i in range(n):
        queue.enqueue(i + 1)
    
    if queue.front is None:
        return None

    res = []
    
    while queue.length > 1:
        discarded = queue.dequeue()
        moved = queue.dequeue()
        res.append(str(discarded))
        queue.enqueue(moved)
    
    res.append(str(queue.dequeue()))
    return ", ".join(res)

def q2(n, k):
    queue = Queue()
    
    for i in range(n):
        queue.enqueue(i + 1)
    
    if queue.front is None:
        return None
    
    res = []

    while queue.length > 1:
        for i in range(k-1): 
            moved = queue.dequeue()
            queue.enqueue(moved)
        discarded = queue.dequeue()
        res.append(str(discarded))

    res.append(str(queue.dequeue()))
    return ", ".join(res)

print(q2(10, 3))