o,m = input(), []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)
if o == "S":
    s = 0
    c = 1
    for i in range(0, 11):
        for j in range(c, 12):
            s = s + m[i][j]
        c = c + 1
    print("{:.1f}".format(s))
if o == "M":
    s = 0
    c = 1
    c2=0
    for i in range(0,11):
        for j in range(c,12):
            s = s + m[i][j]
            c2= c2 + 1
        c = c + 1
    m=s/(c2)
    print("{:.1f}".format(m))

# Codigo velho:

#def S():
#    soma = 0
#    for a in range (12):
#        for i in range(12):
#            if i != 12:
#                soma += L12[a][i+1]
#            if i == 12:
#                soma += L12[a][i]
#    return soma
    
#def M():
#    media = 0
 #   soma = 0
  #  for a in range(12):
   #     for i in range(12):
    #        if i != 12:
     #           soma += L12[a][i+1]
      #      if i == 12:
       #         soma += L12[a][i]
    #media = soma/12
    #return media

#L12 = [
 #   [0,0,0,0,0,0,0,0,0,0,0,0],
  #  [0,0,0,0,0,0,0,0,0,0,0,0],
   # [0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0]
#]
#OP = input()
#for a in range(12):
#    for i in range(12):
 #       NUM = float(input())
  #      L12[a][i] = NUM
#if OP == "S":
 #   r1 = S()
  #  print("{:.1f}".format(r1))
#if OP == "M":
 #   r2 = M()
  #  print("{:.1f}".format(r2))
