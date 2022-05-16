for I in range(100001):
    X,Y = map(int,input().split())
    if X > Y:
        print("Decrescente")
    if Y > X:
        print("Crescente")
    elif X == Y:
        break
