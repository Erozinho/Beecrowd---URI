FIBONACCI,A,N = [0,1],0,int(input())
while A < 120:
    FIBONACCI.append(FIBONACCI[A]+FIBONACCI[A+1])
    A += 1
for x in range(N):
    B = int(input())
    print("Fib({}) = {}".format(B,FIBONACCI[B]))
