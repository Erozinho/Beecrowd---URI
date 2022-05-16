for I in range(10001):
    X,Y = map(int,input().split())
    if Y == 0 or X == 0:
        break
    if X > 0 and Y > 0:
        print("primeiro")
    if X < 0 and Y > 0:
        print("segundo")
    if X < 0 and Y < 0:
        print("terceiro")
    if X > 0 and Y < 0:
        print("quarto")
