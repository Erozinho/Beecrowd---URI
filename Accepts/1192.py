NUM_TESTE = int(input())
for x in range(NUM_TESTE):
    CASO = input()
    if CASO[0] == CASO[2]:
        print(int(CASO[0]) * int(CASO[2]))
    elif CASO[1].isupper():
        print(int(CASO[2]) - int(CASO[0]))
    else:
        print(int(CASO[0]) + int(CASO[2]))
