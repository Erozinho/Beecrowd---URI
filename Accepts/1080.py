TIMER = 0
for X in range(0, 100):
    NUM = int(input())
    if NUM > TIMER:
        MAX = NUM
        POS = X + 1
        TIMER = NUM
print("{}".format(MAX))
print("{}".format(POS))
