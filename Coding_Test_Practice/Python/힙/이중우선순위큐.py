import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    entry_finder = {}
    for operation in operations:
        if operation[0] == 'I':
            num = int(operation[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_finder[num] = entry_finder.get(num, 0) + 1
        elif operation == 'D 1':
            while max_heap and not entry_finder.get(-max_heap[0], 0):
                heapq.heappop(max_heap)
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                entry_finder[max_val] -= 1
                if entry_finder[max_val] == 0:
                    del entry_finder[max_val]
        elif operation == 'D -1':
            while min_heap and not entry_finder.get(min_heap[0], 0):
                heapq.heappop(min_heap)
            if min_heap:
                min_val = heapq.heappop(min_heap)
                entry_finder[min_val] -= 1
                if entry_finder[min_val] == 0:
                    del entry_finder[min_val]
    while max_heap and not entry_finder.get(-max_heap[0], 0):
        heapq.heappop(max_heap)
    while min_heap and not entry_finder.get(min_heap[0], 0):
        heapq.heappop(min_heap)
    if not min_heap or not max_heap:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]