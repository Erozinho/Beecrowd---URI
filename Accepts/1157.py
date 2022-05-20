N = int(input())
for x in range(1,10001):
    if N % x == 0 and x <= N:
        print(x)
