N,A,A1 = int(input()),1,1
for X in range(1, N + 1):
    print("{} {} {}".format(A,A*A,A*A1))
    print("{} {} {}".format(A,(A*A)+1,(A*A1)+1))
    A += 1
    A1 = A * A
