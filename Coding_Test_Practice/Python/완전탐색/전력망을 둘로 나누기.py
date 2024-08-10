from collections import defaultdict
from collections import deque
def solution(n, wires):
    def bfs(node, visited, graph):
        queue = deque([node])
        count = 0
        while queue:
            current = queue.popleft()
            if not visited[current]:
                visited[current] = True
                count += 1
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        return count
    answer = float('inf')
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in wires:
        visited = [False] * (n + 1)
        visited[a] = True
        count1 = bfs(b, visited, graph)
        count2 = n - count1
        answer = min(answer, abs(count1 - count2))
    
    return answer