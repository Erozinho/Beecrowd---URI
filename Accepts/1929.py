VAL = list(map(int,input().split()))
VAL.sort()
if VAL[0] + VAL[1] > VAL[2] and VAL[1] + VAL[2] > VAL[0] and VAL[0] + VAL[2] > VAL[1]:
    print("S")
elif VAL[1] + VAL[2] > VAL[3] and VAL[2] + VAL[3] > VAL[1] and VAL[1] + VAL[3] > VAL[2]:
    print("S")
elif VAL[0] + VAL[2] > VAL[3] and VAL[2] + VAL[3] > VAL[0] and VAL[0] + VAL[3] > VAL[2]:
    print("S")
elif VAL[0] + VAL[1] > VAL[3] and VAL[1] + VAL[3] > VAL[0] and VAL[0] + VAL[3] > VAL[1]:
    print("S")
else:
    print("N")
