def fnc(i):
    K = 6
    if i == K:
        print(result)
        return

    for x in data:
        i, j = x
        result[i], result[j] = result[j], result[i]
        fnc(i+1)





T = int(input())

for tc in range(1, T + 1):
    numbers, change = map(int, input().split())
    numbers = list(map(int, str(numbers)))

    N = len(numbers)
    data = []
    arr = []
    result = numbers[:]

    for a in range(N):
        for b in range(a, N):
            data.append((a, b))
    #print(data)
    fnc(0)