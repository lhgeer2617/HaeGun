T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    max = 0
    i = 0

    cost = 0
    cnt = 0
    result = 0
    
    while i < N-1:

        for x in range(i, N):
            if data[max] < data[x]:
                max = x

        if i == max:
            i += 1
            max = 0
            continue

        for x in range(i, max):
            cost += data[x]
            cnt += 1

        result += ((data[max] * cnt) - cost)
        cnt = 0
        cost = 0
        i = max + 1
        max = 0


    print(f'#{tc} {result}')
