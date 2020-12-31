from collections import deque
import sys

input=sys.stdin.readline
N, K=map(int, input().split())
A=deque(map(int, input().split()))
answer=0
robot=deque([0]*(N*2))

while(True):
    A.rotate(1)
    robot.rotate(1)
    robot[N-1]=0

    for i in range(N-2, -1, -1):
        if(robot[i]!=0 and robot[i+1]==0 and A[i+1]>=1):
            A[i+1]-=1
            robot[i+1]=robot[i]
            robot[i]=0
    robot[N-1]=0

    if(robot[0]==0 and A[0]>0):
        A[0]-=1
        robot[0]=1
    
    cnt=0
    for i in range(N*2):
        if(A[i]==0):
            cnt+=1
    answer+=1
    if(cnt>=K):
        print(answer)
        break
    