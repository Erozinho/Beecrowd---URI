N,num = int(input()),[]
L = list(map(int,input().split()))
for i in range(N):
    num.insert(i,L[i])
for x in range(N):
    if num[x] == min(num):
        pos = x
print("Menor valor: {}\nPosicao: {}".format(min(num), pos))

# Codigo velho:

#num,men,pos = [],0,0
#N = int(input())
#num = list(map(int,input().split()))
#if len(num) == N:
#    for x in range(N):
#        if x == 0:
#            men = num[x]
#        else:
#            if num[x] < men:
#                men = num[x]
#    for i, v in enumerate(num):
#        if v == men:
#            pos = i
#else:
#    quit()
#print("Menor valor: {}\nPosicao: {}".format(men, pos))
