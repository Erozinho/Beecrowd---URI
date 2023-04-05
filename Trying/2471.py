N = int(input())
quadrado = []
for x in range(N):
    nuns = list(map(int, input().split()))
    quadrado.append(nuns)

for x in range(N):
    print(sum(quadrado[x]))
    
