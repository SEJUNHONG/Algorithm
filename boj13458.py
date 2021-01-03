import math

N=int(input())
A=list(map(int, input().split()))
B, C=map(int, input().split())
answer=N

for i in range(len(A)):
    num=A[i]
    num=num-B
    num=math.ceil(num/C)
    answer+=num

print(answer)