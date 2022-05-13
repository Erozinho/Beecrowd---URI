TIMER = 0
SOMA = 0
for X in range(0, 6):
    A = float(input())
    if A > 0:
        SOMA = A + SOMA
        TIMER = TIMER + 1
print("{} valores positivos\n{:.1f}".format(TIMER, (SOMA/TIMER)))
