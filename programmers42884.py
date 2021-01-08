routes=[[-20,15],[-14,-5],[-18,-13],[-5,-3]]

def solution(routes):
    answer=0
    camera=-30000
    start, end=0, 1
    routes=sorted(routes, key=lambda x:x[0])
    check=[0]*len(routes)
    for i in range(len(routes)):
        if check[i]:
            continue
        answer+=1
        camera=routes[i][end]
        for i in range(i, len(routes)):
            if routes[i][start]<=camera and routes[i][end]>=camera:
                check[i]=1
    return answer

print(solution(routes))