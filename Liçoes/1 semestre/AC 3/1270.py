A,B = int(input()),int(input())
if A <= B:
    for x in range(A,B+1):
        for i in range(1,11):
            print("{} x {} = {}".format(x,i,i*x))
            if i == 10: print("-"*10)
else:print("Nenhuma tabuada no intervalo!")
