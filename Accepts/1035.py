A, B, C, D = map(int,input().split())
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 ==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

# Codigo velho:

#x = input().split(" ")
#A, B, C, D = x
#A = int(A)
#B = int(B)
#C = int(C)
#D = int(D)
#if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 ==0:
    #print("Valores aceitos")
#else:
    #print("Valores nao aceitos")
