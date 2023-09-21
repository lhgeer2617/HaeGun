def fnc(start):
    distance = [[0xffffff] * N for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    si, sj = start

    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]






T = int(input().split())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    fnc((0, 0))