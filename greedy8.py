N, M=map(int, input().split())
weight_list=list(map(int, input().split()))
answer=0

for i in range(len(weight_list)):
    for j in range(i, len(weight_list)):
        if weight_list[i]!=weight_list[j]:
            answer+=1

print(answer)