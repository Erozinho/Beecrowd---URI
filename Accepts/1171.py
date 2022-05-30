NUM_TESTE,NUM = int(input()),{}
for x in range(NUM_TESTE):
    ITEM = int(input())
    if ITEM in NUM:
        NUM[ITEM] += 1
    else:
        NUM[ITEM] = 1
QTD = NUM.keys()
QTD = sorted(QTD)
for i in QTD:
    print("{} aparece {} vez(es)".format(i,NUM[i]))
