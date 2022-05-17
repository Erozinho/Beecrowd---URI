L = {1:"Alcool",2:"Gasolina",3:"Diesel",4:"Fim"}
C,A,G,D = True,0,0,0
while True:
    N = int(input())
    if N in L:
        if N == 1:
            A +=1
        if N == 2:
            G +=1
        if N == 3:
            D +=1
        elif N == 4:
            print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(A,G,D))
            break
    else:
        C = True
