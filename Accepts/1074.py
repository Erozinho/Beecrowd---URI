A=int(input())
for X in range(A):
    A = int(input())
    if A < 0:
        if A % 2 ==0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif A > 0:
        if A % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif A == 0:
        print("NULL")
