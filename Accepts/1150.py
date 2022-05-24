X,Z,Z1 = int(input()),int(input()),2
soma,s = X,1
while Z <= X:
    Z = int(input())
while soma <= Z:
    soma = soma + X + s
    if soma <= Z:
        Z1 = Z1 + 1
        s=s+1
print("{}".format(Z1))
