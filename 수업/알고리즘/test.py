N = 4


def solve(row):
    global cnt

    if row == N:
        print('ok')
        cnt += 1
        return
    for col in range(N):
        if not col_check[col] and not dia_check1[row + col] and \
                not dia_check2[N - 1 + row - col]:
            col_check[col] += 1
            dia_check1[row + col] += 1
            dia_check2[N - 1 + row - col] += 1
            solve(row + 1)
            col_check[col] -= 1
            dia_check1[row + col] -= 1
            dia_check2[N - 1 + row - col] -= 1


cnt = 0
col_check = [0] * N
dia_check1 = [0] * (2 * N - 1)
dia_check2 = [0] * (2 * N - 1)

solve(0)
print(cnt)