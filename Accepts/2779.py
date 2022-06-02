N_RESTANTE, COMPRADAS = int(input()),int(input())
ALBUM = [0] * N_RESTANTE
for x in range(COMPRADAS):
    COMPRADAS -= 1
    ALBUM[int(input()) - 1] = 1
print("{}".format(ALBUM.count(0)))
