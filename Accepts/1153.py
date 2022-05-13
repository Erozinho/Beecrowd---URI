N = int(input())
F = 1
TIMER = 1
while TIMER <= N:
    F = F * TIMER
    TIMER = TIMER + 1
print("{}".format(F))
