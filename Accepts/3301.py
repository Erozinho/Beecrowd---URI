idades = list(map(int,input().split()))
for x in range(3):
    if idades[x] != min(idades) and idades[x] != max(idades) and idades.index(idades[x]) == 0:
        print("huguinho")
        break
    if idades[x] != min(idades) and idades[x] != max(idades) and idades.index(idades[x]) == 1:
        print("zezinho")
        break
    if idades[x] != min(idades) and idades[x] != max(idades) and idades.index(idades[x]) == 2:
        print("luisinho")
        break
