T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, 1]
    dc = [1, 0 -1, 0]

    num = 1
    r, c = 0, 0
    x = 0

    while True:
        if num > N*N:
            break

        arr[r][c] = num

        nr = r + dr[x]
        nc = c + dc[x]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            pass
        else:
            x = (x+1)%4

    print(arr)