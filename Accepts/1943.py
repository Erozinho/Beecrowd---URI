N = int(input())
if N == 1:
    print("Top 1")
elif N > 1 and N <= 3:
    print("Top 3")
elif N > 3 and N <= 5:
    print("Top 5")
elif N > 5 and N <= 10:
    print("Top 10")
elif N > 10 and N <= 25:
    print("Top 25")
elif N > 25 and N <= 50:
    print("Top 50")
elif N > 50 and N <= 100:
    print("Top 100")
