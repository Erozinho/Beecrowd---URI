V = list(map(int,input().split()))
if V[0] > V[1] > V[2] > V[3] > V[4]:
    print("D")
elif V[4] > V[3] > V[2] > V[1] > V[0]:
    print("C")
else:
    print("N")
