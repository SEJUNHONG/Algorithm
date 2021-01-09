N=input()
num=len(N)
left, right=0,0
for i in range(int(num/2)):
    left+=int(N[i])
for i in range(int(num/2), num):
    right+=int(N[i])
if left==right:
    print("LUCKY")
else:
    print("READY")