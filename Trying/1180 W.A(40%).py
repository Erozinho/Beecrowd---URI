num,men,pos = [],0,0
N = int(input())
num = list(map(int,input().split()))
if len(num) == N:
    for x in range(N):
        if x == 0:
            men = num[x]
        else:
            if num[x] < men:
                men = num[x]
    for i, v in enumerate(num):
        if v == men:
            pos = i
else:
    quit()
print("Menor valor: {}\nPosicao: {}".format(men, pos))
