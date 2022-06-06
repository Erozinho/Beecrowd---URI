CHAR,POR = input(),0
TEXTO = input().split()
for x in TEXTO:
    if CHAR in x: POR += 1
print("{:.1f}".format(POR/(len(TEXTO)/100)))
