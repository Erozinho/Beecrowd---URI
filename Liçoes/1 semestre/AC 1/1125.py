NOTA_TRAB = float(input())
NOTA_PROV = float(input())
NOTA_SUB = 10.00
MEDIAF = (NOTA_PROV + NOTA_TRAB) / 2.00
MEDIASUB = (NOTA_SUB + NOTA_TRAB) / 2.00
if MEDIAF >= 6.00 and NOTA_TRAB >= 0 and NOTA_TRAB <= 10 and NOTA_PROV >= 0 and NOTA_PROV <= 10:
    print("aprovado")
elif MEDIASUB < 6.00 and MEDIAF < 6.00 and NOTA_TRAB >= 0 and NOTA_TRAB <= 10 and NOTA_PROV >= 0 and NOTA_PROV <= 10:
    print("reprovado")
elif MEDIASUB >= 6.00 and NOTA_TRAB >= 0 and NOTA_TRAB <= 10 and NOTA_PROV >= 0 and NOTA_PROV <= 10:
    print("talvez com a sub")
