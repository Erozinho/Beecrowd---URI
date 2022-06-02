while True:
    try:
        V,D = float(input()),float(input())
        print("ALTURA = {:.2f}".format(V/(3.14*(pow((D/2.0), 2)))))
        print("AREA = {:.2f}".format(3.14*(pow((D/2.0), 2))))
    except EOFError:
        break
