import math
a,b,c = map(int,input().split())
maior = ((a + b + abs(a - b))  / 2)
resultado = (maior + c + abs(maior - c))/2
print("{:.0f} eh o maior".format((maior + c + abs(maior - c))/2))

# Codigo velho:

#import math
#valor = input().split(" ")
#a, b, c = valor
#maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
#resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2
#print("{:.0f} eh o maior".format(resultado))
