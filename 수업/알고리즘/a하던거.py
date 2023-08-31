def fnc(i):
    global max_v, copy_arr
    if i == K:
        print(result)
        for x in result:
            copy_arr[x[0]], copy_arr[x[1]] = copy_arr[x[1]], copy_arr[x[0]]

        st = int(''.join(copy_arr))
        copy_arr = numbers[:]
        if max_v < st:
            max_v = st

        return

    for x in data:
        result[i] = x

        fnc(i + 1)


T = int(input())
for tc in range(1, T + 1):
    numbers, K = map(int, input().split())
    numbers = list(str(numbers))

    copy_arr = numbers[:]
    max_v = 0
    N = len(numbers)
    data = []
    for a in range(N):
        for b in range(a+1, N):
            data.append((a, b))

    result = [0] * K

    fnc(0)
    print(f'#{tc} {max_v}')
