from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    tickets.sort()
    for start, end in tickets:
        graph[start].append(end)
    path = []
    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop(0)
            dfs(next_node)
        path.append(node)
    dfs("ICN")
    return path[::-1]