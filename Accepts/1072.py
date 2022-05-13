A = int(input())
IN = 0
OUT = 0
for X in range(A):
    B = int(input())
    if B >= 10 and B <= 20:
        IN = IN + 1
    else:
        OUT = OUT + 1
print("{} in\n{} out".format(IN,OUT))
