TUBO, QTD = map(int,input().split())
if TUBO == QTD: print(TUBO)
else:print("{}".format((((QTD-1) - TUBO)**2) * 1 + (QTD - 1)))
