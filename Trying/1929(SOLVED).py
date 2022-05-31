VAL = list(map(int,input().split()))
VAL.sort()
if VAL[3] >= VAL[0] + VAL[1] and VAL[3] >= VAL[0] + VAL[2] and VAL[3] >= VAL[1] + VAL[2]:
    print("N")
else:
    print("S")
