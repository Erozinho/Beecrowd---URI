I,X,Q = 0,0,0
while True:
    I = int(input())
    if(I >= 0):
        X += I
        Q += 1
    else:break
print("{:.2f}".format(X/float(Q)))
