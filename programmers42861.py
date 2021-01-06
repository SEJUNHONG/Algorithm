n=4
costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    answer=0
    costs.sort(key=lambda x: x[2])
    union=[i for i in range(n)]
    
    for start, end, cost in costs:
        if union[start]!=union[end]:
            des=union[end]
            for i in range(n):
                if union[i]==des:
                    union[i]=union[start]
            answer+=cost

    return answer

print(solution(n, costs))