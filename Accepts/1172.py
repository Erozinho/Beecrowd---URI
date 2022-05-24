L = []
for a in range(10):
    NUM = int(input())
    if NUM <= 0:
        L.append(1)
    else:
        L.append(NUM)
for i in range(10):
    print("X[{}] = {}".format(i,L[i]))
