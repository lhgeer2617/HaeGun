def f(i, N, K):
    if i == K:
        print(result)
        return

    for j in range(N):
        if not used[j]:
            result[i] = card[j]
            used[j] = 1
            f(i + 1, N, K)
            used[j] = 0


def f2(i):
    if i == 4:
        result = []
        for x in range(len(bit)):
            if bit[x]:
                result.append(data[x])
        print(result)
        return

    bit[i] = 1
    f2(i + 1)
    bit[i] = 0
    f2(i + 1)


def f3():
    a = [1, 2, 3, 4]
    N = 4
    for i in range(1, 1 << (N - 1)):
        result1 = []
        result2 = []
        for j in range(N):
            if i & (1 << j):
                result1.append(a[j])
            else:
                result2.append(a[j])
        print(result1, result2)


N = 5
K = 3
card = [1, 2, 3, 4, 5]
used = [0] * N
result = [0] * K
f(0, N, K)

data = [1, 2, 3, 4]
bit = [0] * 4

# f2(0)

#f3()
