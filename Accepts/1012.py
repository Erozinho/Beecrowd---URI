VALOR = input().split(" ")
A, B, C = VALOR
N = 3.14159
ATRI = (float(A)) * (float(C)) / 2
ACIR = N * (float(C)) ** 2
ATRAP = ((float(B)) + (float(A))) * (float(C)) / 2
AQUAD = (float(B)) * (float(B))
ARET = (float(A)) * (float(B))
print("TRIANGULO: {:.3f}".format(ATRI))
print("CIRCULO: {:.3f}".format(ACIR))
print("TRAPEZIO: {:.3f}".format(ATRAP))
print("QUADRADO: {:.3f}".format(AQUAD))
print("RETANGULO: {:.3f}".format(ARET))
