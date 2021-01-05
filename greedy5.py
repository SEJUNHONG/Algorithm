N, K=map(int, input().split())
answer=0

while True:
    if N==1:
        break
    if N%K==0:
        answer+=1
        N=N/K
    else:
        answer+=1
        N=N-1

print(answer)