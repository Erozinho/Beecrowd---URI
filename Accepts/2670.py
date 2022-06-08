PESSOAS = [int(input()) for andar in range(3)]
MIN = []
MIN.append(PESSOAS[0]*4 + PESSOAS[1]*2)
MIN.append(PESSOAS[0]*2 + PESSOAS[2]*2)
MIN.append(PESSOAS[1]*2 + PESSOAS[2]*4)
MIN.sort()
print(MIN[0])
