start=input()
x,y=(int(ord(start[0])-96)), int(start[1])
move_types=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
answer=0

for move in move_types:
    nx=x+move[0]
    ny=y+move[1]
    if nx>=1 and ny>=1 and nx<=8 and nx<=8:
        answer+=1

print(answer)