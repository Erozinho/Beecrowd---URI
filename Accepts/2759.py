while True:
    try:
        A,B,C = input(),input(),input()
        print("A = {}, B = {}, C = {}".format(A,B,C))
        print("A = {}, B = {}, C = {}".format(B,C,A))
        print("A = {}, B = {}, C = {}".format(C,A,B))
    except EOFError:
        break
