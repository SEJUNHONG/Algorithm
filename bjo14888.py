N=int(input())
num_list=list(map(int, input().split()))
add, sub, mul, div=map(int, input().split())
max_num, min_num=-99999, 99999

def solution(num, result, add, sub, mul, div):
    global max_num, min_num
    if num==N:
        max_num=max(result, max_num)
        min_num=min(result, min_num)
        return 

    else:
        if add:
            solution(num+1, result+num_list[num], add-1, sub, mul, div)
        if sub:
            solution(num+1, result-num_list[num], add, sub-1, mul, div)
        if mul:
            solution(num+1, result*num_list[num], add, sub, mul-1, div)
        if div:
            solution(num+1, int(result/num_list[num]), add, sub, mul, div-1)

solution(1, num_list[0], add, sub, mul, div)
print(max_num)
print(min_num)