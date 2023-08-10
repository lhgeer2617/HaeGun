T = int(input())
for tc in range(1, T+1):
    stack = []             # 쇠막대기를 스택에 넣어 보관하고 레이저가 보관된만큼 자를 것이다.
    input_str = input()
    cnt = 0                # 레이저가 쇠막대기를 자르는 수를 셀것이다(그만큼 쇠막대기 수가 증가)
    num = 0                # 쇠막대기가 몇개인지 세어줄것이다.
    for i in range(len(input_str)):
        if input_str[i] == '(' and input_str[i + 1] == ')':  # () 이 둘이 붙어 있으면 레이저이다.
            cnt += len(stack)                                # 레이저는 막대기 갯수만큼 자를 것이다.
        elif input_str[i] == '(':                            # ( 가 혼자있다면 막대기의 시작점이다. 그만큼 스택에 추가
            stack.append(input_str[i])
            num += 1                                         # append 될때마다 num을 증가시켜 쇠막대기 갯수를 구한다.
        elif input_str[i] == ')' and input_str[i - 1] != '(':  # )가 혼자 있다면 막대기의 끝지점이가. 막대기를 스택에서 하나 빼준다.
            stack.pop()
    print(f'#{tc} {cnt + num}')                              # 총 막대기 갯수와 잘라내서 생겨난 수를 더해준다.
