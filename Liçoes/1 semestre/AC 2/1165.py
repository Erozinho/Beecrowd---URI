C = 0
while True:
    N = float(input())
    if N <= -1:
        break
    C += N
print("VC$ {:.2f}\nR$ {:.2f}".format(C,C*2.5))
