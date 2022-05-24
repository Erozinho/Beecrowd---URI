L = []
NUM = int(input())
L.append(NUM)
for a in range(10):
    L.append(L[a]*2)
for i in range(10):
    print("N[{}] = {}".format(i,L[i]))
