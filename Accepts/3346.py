N1,N2 = map(float,input().split())
print("{:.6f}".format(((((1.0 + N1/100.00) * (1.0 + N2/100.00)) - 1.0) * 100.0)))
