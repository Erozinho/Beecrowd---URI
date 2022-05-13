A = int(input())
B = int(input())
X = 0
for I in range((B+1),A):
    if (I % 2 != 0):
        X += I
print(X)
