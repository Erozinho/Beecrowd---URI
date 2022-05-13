DIAS = int(input())
A = DIAS//365
DIAS = DIAS-A*365
M = DIAS//30
DIAS = DIAS-M*30
D = DIAS
print("{} ano(s)".format(A))
print("{} mes(es)".format(M))
print("{} dia(s)".format(D))
