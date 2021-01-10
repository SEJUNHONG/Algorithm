def solution(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

N=int(input())
num_list=list(map(int, input().split()))
answer=0

for i in range(N):
    if solution(num_list[i]):
        answer+=1

print(answer)