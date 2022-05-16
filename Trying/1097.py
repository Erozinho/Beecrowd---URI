I, J = 1, 7
while I <= 9:
    if I == 1:
        while J >= 5:
            print("I={} J={}".format(I,J))
            J = J - 1
    if I == 3:
        while J >= 7:
            print("I={} J={}".format(I,J))
            J = J - 1
    if I == 5:
        while J >= 9:
            print("I={} J={}".format(I,J))
            J = J - 1
    if I == 7:
        while J >= 11:
            print("I={} J={}".format(I,J))
            J = J - 1
    if I == 9:
        while J >= 13:
            print("I={} J={}".format(I,J))
            J = J - 1
    I = I + 2
    J = J + 2
