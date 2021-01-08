food_times=[3,1,2]
k=5

def solution(food_times, k):
    answer=0
    result=0
    while True:
        cnt=0
        for i in range(len(food_times)):
            if result==k+1:
                return answer
            if food_times[i]==0:
                cnt+=1
                pass
            else:
                food_times[i]-=1
                result+=1
                answer=i+1
            if cnt==(len(food_times)-1):
                return -1

print(solution(food_times, k))