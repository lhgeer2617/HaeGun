N, M = map(int, input().split())

numbers = [x for x in range(N+1)]
reverse_range = []
for x in range(M):
    reverse_range.append(list(map(int, input().split())))

for num in reverse_range:
    i = 0
    x = num[0]
    y = num[1]
    while x != y:
        
        temp = numbers[x]
        numbers[x] = numbers[y]
        numbers[y] = temp


        i += 1
        x += i
        y -= i

        if abs(x-y) == 1:
            break

for x in range(1, N+1):
    print(numbers[x], end=' ')