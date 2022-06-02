L = int(input())
C = int(input())
if L == C:
    print(1)
elif L % 2 == 0 and C % 2 == 0:
    print(1)
elif L % 2 != 0 and C % 2 != 0:
    print(1)
elif L % 2 == 0 and C % 2 != 0 or L % 2 != 0 and C % 2 == 0:
    print(0)
