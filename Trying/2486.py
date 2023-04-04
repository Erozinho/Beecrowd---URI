while True:
    alimentos={"suco de laranja":120, "morango fresco":85,
    "mamao":85, "goiaba vermelha":70, "manga":56, "laranja":50, "brocolis":34}
    
    n = int(input())
    if n == 0:
        break
    total=[]
    for x in range(n+1):
        vezes,comida= map(str, input().split())
        vezes = int(vezes)
        total.append(vezes*alimentos[comida])
    if 110 >= sum(total) <= 130:
        print(f"{sum(total)} mg")
