N_ANOS = int(input())
for x in range(N_ANOS):
    ANO = int(input())
    if ANO >= 2015:print("{} A.C.".format(ANO-2015+1))
    else:print("{} D.C.".format(2015-ANO))
