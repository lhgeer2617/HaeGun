def fnc(i):

    if i == change:
        print(arr)
        return

    for x in data:
        arr[i] = x
        fnc(i+1)


def fnc2(i):
    if i == len(bit):
        for x in range(len(bit)):
            if bit[x]:
                print(data[x], end=' ')
        print()
        return

    bit[i] = 1
    fnc2(i + 1)
    bit[i] = 0
    fnc2(i + 1)






T = int(input())

for tc in range(1, T + 1):
    numbers, change = map(int, input().split())
    numbers = list(map(int, str(numbers)))

    N = len(numbers)
    data = []
    arr = [0] * change
    result = numbers[:]
    visited = [0] * 6

    for a in range(N):
        for b in range(a, N):
            data.append((a, b))

    M = len(data)

    bit = [0] * change
    tt = [1, 2, 3]
    print(data)
    fnc(0)
    #fnc(0)
    # for x in data:
    #     i, j = x
    #     result[i], result[j] = result[j], result[i]
    #print(result)