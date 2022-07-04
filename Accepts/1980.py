while True:
    EMBA = 1
    LETRAS = input().split()[0]
    if LETRAS == "0":break
    for x in range(1, len(LETRAS)+1):EMBA *= x
    print(EMBA)
