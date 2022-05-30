x = 99999
while True:
    x = input().split()
    if x == ['0']:
        break
    A,B,C = x
    A, B, C = int(A), int(B), int(C)
    print("{:.0f}".format(pow(((A*B)*100)/C, 0.5)))
