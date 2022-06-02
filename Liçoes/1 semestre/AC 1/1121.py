PRICE = float(input())
QUANT = int(input())
VALORT = PRICE * QUANT
DESCONTO = 0.1 + (QUANT / 100)
VALORD = VALORT * DESCONTO
print("{:.2f}".format(VALORT))
print("{:.2f}".format(VALORT - VALORD))