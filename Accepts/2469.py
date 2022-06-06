NUM = int(input())
NOTAS = input().split()
print("{}".format(max(set(NOTAS), key=NOTAS.count)))
