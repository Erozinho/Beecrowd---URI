A,B = map(int,input().split())
if A < B:
    C = B - A
else:
    C = (24 - A) + B
print("O JOGO DUROU {} HORA(S)".format(C))

# Codigo velho:

#NUM = input().split()
#A, B = NUM
#A = int(A)
#B = int(B)
#if A < B:
    #C = B - A
#else:
    #C = (24 - A) + B
#print("O JOGO DUROU {} HORA(S)".format(C))
