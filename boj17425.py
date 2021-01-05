
T=int(input())

def yaksu(n):
    gx=0
    for i in range(n+1):
        for j in range(i, 0, -1):
            if i%j==0:
                gx+=j
    return gx

for _ in range(T):
    N=int(input())
    print(yaksu(N))