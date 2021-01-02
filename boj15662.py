from collections import deque

T=int(input())
circle=[deque(map(int, input())) for _ in range(T)]
oper=deque(list(map(int, input().split())) for _ in range(int(input())))

while oper:
    num, direct=oper.popleft()
    num-=1
    three=circle[num][2]
    nine=circle[num][6]
    circle[num].rotate(direct)
    dire=direct

    direct=dire
    for i in range(num-1, 0-1, -1):
        if circle[i][2]!=nine:
            nine=circle[i][6]
            circle[i].rotate(direct*-1)
            direct*=-1
        else:
            break

    direct=dire
    for i in range(num+1, T):
        if circle[i][6]!=three:
            three=circle[i][2]
            circle[i].rotate(direct*-1)
            direct*=-1
        else:
            break
answer=0
for i in range(T):
    if circle[i][0]==1:
        answer+=1
print(answer)