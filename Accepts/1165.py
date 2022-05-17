N = int(input())
for i in range(N):
    X,count = int(input()),0
    for i in range(1, X + 1):
        if X % i == 0:
            count += 1
    if count != 2:
        print('{0} nao eh primo'.format(X))
    elif count == 2:
        print('{0} eh primo'.format(X))
