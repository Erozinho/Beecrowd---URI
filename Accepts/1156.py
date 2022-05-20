S,X= 0,1
for  I in range(1,40,2):
    S = S+I/X
    X *= 2
print("{:.2f}".format(S))
