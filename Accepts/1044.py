A,B = map(int,input().split())
if A > B and A % B == 0 or A == B:
    print("Sao Multiplos")
if A < B and B % A == 0:
    print("Sao Multiplos")
elif A < B and B % A != 0 or A > B and A % B != 0:
    print("Nao sao Multiplos")
    
# Codigo velho:

#A,B = map(int,input().split())
#if A > B and A % B == 0:
        #print("Sao Multiplos")
#else:
      #print("Nao sao Multiplos")
#if A < B:
    #if B % A == 0:
        #print("Sao Multiplos")
    #else:
        #print("Nao sao Multiplos")
#else:
    #print("Sao Multiplos")
