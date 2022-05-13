NUM = input().split()
C, Q = NUM
if C == "1":
    print("Total: R$ {:.2f}".format(4.00 * float(Q)))
if C == "2":
    print("Total: R$ {:.2f}".format(4.50 * float(Q)))
if C == "3":
    print("Total: R$ {:.2f}".format(5.00 * float(Q)))
if C == "4":
    print("Total: R$ {:.2f}".format(2.00 * float(Q)))
if C == "5":
    print("Total: R$ {:.2f}".format(1.50 * float(Q)))
