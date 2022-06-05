CONSUMO = int(input())
if CONSUMO <= 10:
    print(7)
elif 11 <= CONSUMO <= 30:
    print("{}".format((CONSUMO-10) * 1 + 7))
elif 31 <= CONSUMO <= 100:
    print("{}".format((CONSUMO*2)- 40 + 7))
else:
    print("{}".format(((CONSUMO*5)- 340 + 7)))
