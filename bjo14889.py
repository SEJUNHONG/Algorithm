from itertools import combinations

N=int(input())
match=[]
for _ in range(N):
    match.append(list(map(int, input().split())))
team_list=[i for i in range(N)]
answer=10000

def solution():
    global answer
    for comb in combinations(team_list, N//2):
        start=list(comb)
        link=list(set(team_list)-set(comb))

        s_comb=list(combinations(start, 2))
        l_comb=list(combinations(link, 2))

        result1=0
        for i,j in s_comb:
            result1+=(match[i][j]+match[j][i])
        result2=0
        for i,j in l_comb:
            result2+=(match[i][j]+match[j][i])

        if(answer>abs(result1-result2)):
            answer=abs(result1-result2)
solution()
print(answer)