VAL= list(map(int,input().split()))
VAL.sort()
if VAL[3]>(VAL[0]+VAL[1]) and VAL[3]>(VAL[2]+VAL[1]) and VAL[3]>(VAL[2]+VAL[0]):
    print("N")
elif VAL[0] == VAL[1] == VAL [2] == VAL[3]:
else:
    print("S")
