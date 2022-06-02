N = int(input())
X = input().split()
for i in range(N):
    X[i] = int(X[i])
print("{}".format(X.index(min(X)) + 1))
