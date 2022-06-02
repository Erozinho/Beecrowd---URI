p,s=0,1
F=[p,s]
NUM = int(input())
for i in range(2,NUM+1):
    t=s+p
    p=s
    s=t
    F.append(t)
F.pop(0)
F.reverse()
print(*F)
