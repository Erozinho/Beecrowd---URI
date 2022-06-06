NUM_FLAVIO = list(map(int,input().split()))
NUM_SORTE = list(map(int,input().split()))
A = 0
for x in range(6):
    if NUM_FLAVIO[x] in NUM_SORTE: A += 1
if A < 3: print("azar")
if A == 3: print("terno")
if A == 4: print("quadra")
if A == 5: print("quina")
if A == 6: print("sena")
