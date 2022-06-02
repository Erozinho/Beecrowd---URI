while True:
    try:
        CPF = input()
        CPF = CPF.replace("-", ".")
        CPF = CPF.split(".")
        for cpf in CPF:
            print("{}".format(cpf))
    except EOFError:
        break
