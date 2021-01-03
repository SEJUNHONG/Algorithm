N=int(input())
fear=list(map(int, input().split()))
fear.sort()
answer=0

while True:
    if N==0:
        break
    if N<fear[N-1]:
        break
    N=N-fear[N-1]
    answer+=1

print(answer)
print(answer)