x = 99999
while True:
    x = input().split()
    if x == ['0']:
        break
    A,B,C = x
    A, B, C = int(A), int(B), int(C)
    D = pow(((A*B)*100)/C, 0.5)
    print("{}".format(int(D)))
