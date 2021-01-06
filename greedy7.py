N=int(input())
num_list=list(map(int, input().split()))
num_list.sort()
answer=1

for i in num_list:
    if answer<i:
        break
    answer+=i

print(answer)