from math import sqrt
while True:
    try:
        Xf,Yf,Xi,Yi,Vi,R1,R2 = map(int,input().split())
        if (sqrt(pow(Xi - Xf, 2.0) + pow(Yi - Yf, 2.0)) + (Vi * 1.50) > R1+R2): print("N")
        else:print("Y")
    except EOFError:
        break
