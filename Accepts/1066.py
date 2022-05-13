PAR = 0
IMP= 0
POS = 0
NEG = 0
for X in range(0, 5):
    A = int(input())
    if A > 0:
        POS = POS + 1
    if A < 0:
        NEG = NEG + 1
    if A % 2 == 0:
        PAR = PAR + 1
    if A % 3:
        IMP = IMP + 1
print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(PAR,IMP,POS,NEG))
