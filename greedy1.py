N, M, K=map(int, input().split())
num_list=list(map(int, input().split()))

num_list.sort()
answer=0
i=0
while True:
    for j in range(K):
        if i==M:
            break
        answer+=num_list[N-1]
        i+=1
    if i==M:
        break
    answer+=num_list[N-2]
    i+=1
print(answer)