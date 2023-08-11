import sys

N = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().rstrip().split()))

top = N - 1
point = top
result = [0] * N

while data:
    num = data.pop()
    top = point
    top -= 1

    if len(data) != 0 and max(data) < num:
        point -= 1
    is_flag = False
    for x in range(point):
        if 0 <= point < len(data) and data[x] < data[x + 1]:
            is_flag = True
        else:
            is_flag = False
            break

    if is_flag:
        break

    while top >= 0:

        if len(data) != 0 and max(data) < num:
            point -= 1
            break

        if data[top] >= num:
            result[point] = top + 1
            point -= 1
            break
        else:
            top -= 1
    else:
        point -= 1

print(*result)
