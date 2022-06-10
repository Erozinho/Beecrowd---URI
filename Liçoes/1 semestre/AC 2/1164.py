N = int(input())
for X in range(N):
    if X == 0:print("{}".format(chr(65+X)))
    else:print("{}".format(chr(65+X)*(X+1)))
