OP,S,C = input(),0,0
for i in range(12):
  for j in range(12):
    valor = float(input())
    if(i >= 7 and i + j >= 12 and j < i):
      S += valor
      C += 1
if OP == "S":
  print("{:.1f}".format(S))
else:
  print("{:.1f}".format(S / C))
