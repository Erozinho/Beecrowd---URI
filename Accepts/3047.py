M,F1,F2 = int(input()),int(input()),int(input())
V = M-(F1+F2)
IDADES = [F1,F2,V]
IDADES.sort()
print("{}".format(IDADES[2]))
