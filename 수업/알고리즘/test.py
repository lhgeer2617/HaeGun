t = 10
for tc in range(1,t+1):
    dump = int(input()) # 덤프 제한 횟수
    arr =list(map(int, input().split()))

    cnt = 0
    arr_index = 0
    cnt_index = 0
    max_h = 0
    min_h = 100

    for i in range(dump):

        for j in arr:
            if max_h < j :
                max_h = j # 리스트 내 최대값 구하기
            if min_h > j :
                min_h = j # 리스트 내 최솟값 구하기

        max_h -= 1
        min_h += 1

        cnt += 1

        result = max_h-min_h

    print(f'#{tc} {result}')