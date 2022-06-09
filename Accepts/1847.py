A,B,C = map(int,input().split())
if(A > B):
    if C > B:print(":)")
    else:
        if(B-C < A-B):print(":)")
        else:print(":(")
elif(A < B):
    if C < B:print(":(")
    else:
        if(B-C > A-B):print(":(")
        else:print(":)")
else:
    if C > A:print(":)")
    else:print(":(")
