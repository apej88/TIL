from d_queue import Queue
def q1(n):
    cards = Queue()
    trash = Queue()
    
    for i in range(1, n+1):
        cards.enqueue(i)
    
    while(len(cards) > 1):
        trash.enqueue(cards.dequeue())
        cards.enqueue(cards.dequeue())
    
    trash.enqueue(cards.dequeue())
    return trash

def q2(n, k):
    queue = Queue()
    dead = []
    
    for i in range(1, n+1):
        queue.enqueue(i)
        
    while not queue.is_empty():
        cnt = 1
        while cnt < k:
            queue.enqueue(queue.dequeue())
            cnt += 1
        
        dead.append(queue.dequeue())
    return dead