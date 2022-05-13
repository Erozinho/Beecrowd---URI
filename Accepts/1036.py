NUM = input().split()
A, B, C = NUM
A = float(A)
B = float(B)
C = float(C)
DEL = (B ** 2) - 4 * A * C
if A != 0 and DEL > 0:
    X1 = (-B + DEL ** (1/2)) / (2 * A)
    X2 = (-B - DEL ** (1/2)) / (2 * A)
    print("R1 = {:.5f}".format(X1))
    print("R2 = {:.5f}".format(X2))
elif A == 0 or DEL < 0:
    print("Impossivel calcular")
