T1,T2,T3 = map(int, input().split())
P1,P2,P3 = map(int, input().split())
A1,A2,A3 = 0,0,0
if T1 < P1:
  A1 = P1 - T1
if T2 < P2:
  A2 = P2 - T2
if T3 < P3:
  A3 = P3 - T3
print("{}".format(A1 + A2 + A3))  
