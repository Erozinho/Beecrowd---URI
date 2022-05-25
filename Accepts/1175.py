L = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for a in range(20):
    NUM = int(input())
    L[(19-a)] = NUM
for i in range(20):
    print("N[{}] = {}".format(i,L[i]))
