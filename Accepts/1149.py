X = input().split()
N1 = int(X[0])
X1 = len(X) -1
N2 = int(X[X1])
soma = 0
for I in range(0, N2):
    soma += N1 + I
print("{}".format(soma))
