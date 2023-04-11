NUM = list(map(int,input().split()))
A, B, C = sorted(NUM)[::-1]
continua = True
if(A >= B+C):
    print("Invalido")
    continua = False
if(A != B and B != C and C != A and continua == True):
    print("Valido-Escaleno")
if(A == B and B == C and continua  == True):
    print("Valido-Equilatero")
if((A == B or B == C) and not (A == B and B == C) and continua  == True):
    print("Valido-Isoceles")
if(A**2 == (B**2) + (C**2) and continua  == True):
    print("Retangulo: S")
if (A**2 != (B**2) + (C**2) and continua  == True):
    print("Retangulo: N")
