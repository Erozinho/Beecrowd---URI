DIAMETRO = int(input())
A,L,P = map(int,input().split())
if A >= DIAMETRO and P >= DIAMETRO and L >= DIAMETRO:
    print("S")
else:
    print("N")
