# str1에 들어있는 문자들이 str에 각각 몇개나 포함이 되어있고
# 그중에서 가장 많이 포함된 문자의 수를 출력

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    # str의 문자들을 딕셔너리의 키값으로 넣고 벨류로
    # str2에 몇개나 있는지를 카운트

    dic = {}

    for x in str1:
        dic.setdefault(x, 0)

    for x in str2:
        try:
            dic[x] += 1
        except KeyError:
            pass
    
    # 벨류의 최대값을 구하면 끝

    data = list(dic.values())

    my_max = -1

    for x in data:
        if my_max < x:
            my_max = x

    print(f'#{tc} {my_max}')