X = int(input())
Y = int(input())
if X > Y:
    A = Y
    B = X
if X <= Y:
    A = X
    B = Y
S = 0
while A <= B:
    if (A % 13 != 0):
        S += A
    A = A + 1
print(S)
