par,impar = [],[]
for i in range(15):
    N = int(input())
    if N % 2 != 0:
        impar.append(N)
    else:
        par.append(N)
    if len(par) == 5:
        for y in range(5):
            print("par[{}] = {}".format(y, par[y]))
        par = []
    if len(impar) == 5:
        for x in range(5):
            print("impar[{}] = {}".format(x, impar[x]))
        impar = []
if len(impar) > 0:
    for m in range(len(impar)):
        print("impar[{}] = {}".format(m, impar[m]))
if len(par) > 0:
    for x in range(len(par)):
        print("par[{}] = {}".format(x, par[x]))
