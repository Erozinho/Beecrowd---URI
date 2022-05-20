A,B,C = map(float,input().split())
print("TRIANGULO: {:.3f}".format((A * C) / 2))
print("CIRCULO: {:.3f}".format(3.14159 * C ** 2))
print("TRAPEZIO: {:.3f}".format(((B + A) * C) / 2))
print("QUADRADO: {:.3f}".format(B * B))
print("RETANGULO: {:.3f}".format(A * B))

# Codigo velho:

#VALOR = input().split(" ")
#A, B, C = VALOR
#N = 3.14159
#ATRI = (float(A)) * (float(C)) / 2
#ACIR = N * (float(C)) ** 2
#ATRAP = ((float(B)) + (float(A))) * (float(C)) / 2
#AQUAD = (float(B)) * (float(B))
#ARET = (float(A)) * (float(B))
#print("TRIANGULO: {:.3f}".format(ATRI))
#print("CIRCULO: {:.3f}".format(ACIR))
#print("TRAPEZIO: {:.3f}".format(ATRAP))
#print("QUADRADO: {:.3f}".format(AQUAD))
#print("RETANGULO: {:.3f}".format(ARET))
