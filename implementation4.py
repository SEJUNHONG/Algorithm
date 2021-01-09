S=input()
answer=[]
num=0
for i in range(len(S)):
    if ord(S[i])>=48 and ord(S[i])<=57:
        num+=int(S[i])
    else:
        answer.append(S[i])
answer.sort()
answer.append(str(num))
print(''.join(answer))