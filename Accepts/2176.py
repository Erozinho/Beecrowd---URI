N,B = input(),0
for i in N:
    if i == '1':
        B += 1
print("{}".format(N + str(B % 2)))
