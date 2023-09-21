def dijkstra(start):
    distance = [[0xffffff] * N for _ in range(N)]
    visited = set(start)
    now_i, now_j = start

    distance[now_i][now_j] = 0
    while len(visited) < V:

        for next in range(V):
            if next not in visited and graph[now][next] != -1:
                if distance[next] > graph[now][next] + distance[now]:
                    distance[next] = graph[now][next] + distance[now]

        min_dis = 0xffffff
        min_node = -1
        for node in range(V):
            if node not in visited and min_dis > distance[node]:
                min_dis = distance[node]
                min_node = node

        now = min_node
        visited.append(now)

    return distance


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    dijkstra((0,0))