
def sosu(n):
    number=[1]*n
    for i in range(2, int(n**0.5)+1):
        if number[i]==1:
            for j in range(i+i, n, i):
                number[j]=0
    return number

number=sosu(1000000)

while True:
    num=int(input())
    if num==0:
        break
    
    for i in range(3, num//2+1):
        if number[i] and number[num-i]:
            print("{} = {} + {}".format(num, i,  num-i))
            break
