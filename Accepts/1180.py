N,num = int(input()),[]
L = list(map(int,input().split()))
for i in range(N):
    num.insert(i,L[i])
for x in range(N):
    if num[x] == min(num):
        pos = x
print("Menor valor: {}\nPosicao: {}".format(min(num), pos))
