VT,VP = int(input()),int(input())
AP = round(VT/VP)
if AP < VT/VP: AP +=1
for x in range(AP):
    A = VT - VP
    if A <= 0: A = 0
    print("pagamento: {}\nantes = {}\ndepois = {}\n-----".format(x+1, VT, A))
    VT -= VP
