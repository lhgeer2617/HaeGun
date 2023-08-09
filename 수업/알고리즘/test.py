class stack:
    def __init__(self):  # 스택 객체 생성
        self.items = []
    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)
    def pop(self):  # 스택 맨 뒤 요소 삭제하고 리턴 pop()
        try:
            self.items.pop()
        except IndexError:
            exit(0)
    def top(self):  # 스택 맨 뒤 요소 리턴
        try:
            return self.items[-1]
        except IndexError:
            exit(0)
    def isEmpty(self):  # 스택이 비었는지 확인(비었으면 True 리턴)
        return not self.items
    def len_stack(self): # 스택 내의 데이터 개수를 확dls
        return len(self.items)

s = stack()
t = int(input())
for tc in range(1, t+1):
    text = input()
    size = len(text)
    stack = [0]*size
    for i in text:
        if i == '{' or i == '[' or i == '(':
            s.push(i)
        elif i == ')':
            if s.top() == '(':
                s.pop()
            else:
                break
        elif i == '}':
            if s.top() == '{':
                s.pop()
            else:
                break
        elif i == ']':
            if s.top() == '[':
                s.pop()
            else:
                break
    if s.len_stack() == 0:
        result = 1
    else :
        result = 0
    print(f'#{tc} {result}')