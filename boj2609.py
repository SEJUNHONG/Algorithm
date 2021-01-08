num1, num2=map(int, input().split())
gcd, lcm=1, 1
if num1>=num2:
    big=num1
    small=num2
else:
    big=num2
    small=num1

for i in range(small, 0, -1):
    if big%i==0 and small%i==0:
        gcd=i
        break

lcm=int(gcd*(big/gcd)*(small/gcd))

print(gcd)
print(lcm)