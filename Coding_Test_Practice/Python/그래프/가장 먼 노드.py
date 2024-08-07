from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    def bfs(node, visited, graph):
        queue = deque([(node, 0)])
        count = []
        while queue:
            current, length = queue.popleft()
            if not visited[current]:
                visited[current] = True
                count.append((current, length))
                length += 1
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        queue.append((neighbor, length))
        return count
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    counts = bfs(1, visited, graph)
    max_length = 0
    max_length_count = 0
    for count in counts:
        if max_length < count[1]:
            max_length = count[1]
    for count in counts:
        if count[1] == max_length:
            max_length_count += 1
    answer = max_length_count
    return answer