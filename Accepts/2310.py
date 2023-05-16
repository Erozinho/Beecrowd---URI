n_jogadores = int(input())
total = [0, 0, 0]
acertos = [0, 0, 0] 
for x in range(n_jogadores):
    nome = str(input())
    s,b,a = map(int, input().split())
    total[0] = total[0] + s
    total[1] = total[1] + b
    total[2] = total[2] + a
    s1,b1,a1 = map(int, input().split())
    acertos[0] = acertos[0] + s1
    acertos[1] = acertos[1] + b1
    acertos[2] = acertos[2] + a1
print(f"Pontos de Saque: {(acertos[0]/total[0]) * 100 :.2f} %.")
print(f"Pontos de Bloqueio: {(acertos[1]/total[1]) * 100 :.2f} %.")
print(f"Pontos de Ataque: {(acertos[2]/total[2]) * 100 :.2f} %.")
