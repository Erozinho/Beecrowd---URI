L = []
for a in range(100):
    NUM = float(input())
    L.append(NUM)
for i in range(100):
    if L[i] <= 10:
        print("A[{}] = {:.1f}".format(i,L[i]))
