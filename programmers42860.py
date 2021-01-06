name="JEROEN"
# name="JAN"

def solution(name):
    answer=0
    idx = 0
    base = 'A' * len(name)
    while(True):
        leftIdx = idx
        rightIdx = idx
        if(name[idx] != 'A'):
            if(ord(name[idx]) - ord('A') > 13):
                answer += 26 - (ord(name[idx]) - ord('A'))
            else:
                answer += ord(name[idx]) - ord('A')
            name = name[0:idx] + 'A' + name[idx+1:]
        if(name == base):
            break
        while(name[leftIdx] == 'A' and name[rightIdx] == 'A'):
            answer += 1
            if(leftIdx == 0):
                leftIdx = len(name) - 1
            else:
                leftIdx -= 1
            if(rightIdx == len(name)-1):
                pass
            else:
                rightIdx += 1
        if(name[rightIdx] != 'A'):
            idx = rightIdx
        else:
            idx = leftIdx
    return answer

print(solution(name))