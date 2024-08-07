def solution(n, results):
    INF = float('inf')
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for winner, loser in results:
        graph[winner - 1][loser - 1] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            answer += 1
    return answer