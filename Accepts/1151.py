p,s=0,1
F=[p,s]
for i in range(2,46):
    t=s+p
    p=s
    s=t
    F.append(t)
NUM = int(input())
for i in range(0, NUM):
    if i != (NUM - 1):
        print("{}".format(F[i]), end=" ")
    else:
        print("{}".format(F[i]))
