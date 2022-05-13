NUM = input().split()
X, Y = NUM
X = float(X)
Y = float(Y)
if X == 0:
    if Y == 0:
        print("Origem")
    if Y != 0:
        print("Eixo Y")
if Y == 0:
    if X != 0:
        print("Eixo X")
if X > 0:
    if Y > 0:
        print("Q1")
    if Y < 0:
        print("Q4")
if X < 0:
    if Y > 0:
        print("Q2")
    if Y < 0:
        print("Q3")
