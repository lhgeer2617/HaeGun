T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()

    time = 0
    cnt = 0
    i = 0
    #ot = 0

    while True:

        if i == N:
            print(f'#{tc} Possible')
            break

        time = data[i] - time
        #time += ot
        #ot = time % M

        cnt += (time // M) * K

        cnt -= 1
        i += 1.

        if cnt < 0:
            print(f'#{tc} Impossible')
            break
