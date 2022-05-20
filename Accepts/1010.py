COD1,Q1,V1 = input().split()
COD2,Q2,V2 = input().split()
print("VALOR A PAGAR: R$ {0:.2f}".format((int(Q1) * float(V1)) + (int(Q2) * float(V2)))) 

# Codigo velho:

#linha1 = input().split(" ")
#linha2 = input().split(" ")
#cod1, qtde1, valor1 = linha1
#cod2, qtde2, valor2 = linha2
#print("VALOR A PAGAR: R$ {0:.2f}".format((int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2)))) 
