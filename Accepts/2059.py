p, j1, j2, r, a = map(int,input().split())
if p == 1 and (j1+j2)%2 == 0 and r == 0: print("Jogador 1 ganha!")
if p == 0 and (j1+j2)%2 != 0 and r == 0: print("Jogador 1 ganha!")
if p == 1 and (j1+j2)%2 != 0 and r == 0: print("Jogador 2 ganha!")
if p == 0 and (j1+j2)%2 == 0 and r == 0: print("Jogador 2 ganha!")
if r == 1 and a == 0:print("Jogador 1 ganha!")
if r == 1 and a == 1:print("Jogador 2 ganha!")