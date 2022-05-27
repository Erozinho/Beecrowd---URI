L = [float(input())]
for x in range(100):
    print("N[{}] = {:.4f}".format(x,L[0]))
    L[0] = L[0]/2
