VT,VP = int(input()),int(input())
AP = round(VT/VP)
if AP < VT/VP: AP +=1
if AP > 0 and AP < 1 : print("pagamento: 1\nantes = {}\ndepois = 0\n-----".format(VT))
else:
    for x in range(AP):
        A = VT - VP
        if A <= 0: A = 0
        print("pagamento: {}\nantes = {}\ndepois = {}\n-----".format(x+1, VT, A))
        VT -= VP
