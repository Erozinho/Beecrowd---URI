NTESTES = int(input())
for x in range(NTESTES):
    S,R = input().split()
    if S == R:print("Caso #{}: De novo!".format(x+1))
    if S == "tesoura":
        if R == "papel":print("Caso #{}: Bazinga!".format(x+1))
        if R == "lagarto":print("Caso #{}: Bazinga!".format(x+1))
        if R == "Spock":print("Caso #{}: Raj trapaceou!".format(x+1))
        if R == "pedra":print("Caso #{}: Raj trapaceou!".format(x+1))
    if S == "papel":
        if R == "pedra":print("Caso #{}: Bazinga!".format(x+1))
        if R == "Spock":print("Caso #{}: Bazinga!".format(x+1))
        if R == "tesoura":print("Caso #{}: Raj trapaceou!".format(x+1))
        if R == "lagarto":print("Caso #{}: Raj trapaceou!".format(x+1))
    if S == "pedra":
        if R == "tesoura":print("Caso #{}: Bazinga!".format(x+1))
        if R == "lagarto":print("Caso #{}: Bazinga!".format(x+1))
        if R == "papel":print("Caso #{}: Raj trapaceou!".format(x+1))
        if R == "Spock":print("Caso #{}: Raj trapaceou!".format(x+1))
    if S == "Spock":
        if R == "pedra":print("Caso #{}: Bazinga!".format(x+1))
        if R == "tesoura":print("Caso #{}: Bazinga!".format(x+1))
        if R == "lagarto":print("Caso #{}: Raj trapaceou!".format(x+1))
        if R == "papel":print("Caso #{}: Raj trapaceou!".format(x+1))
    if S == "lagarto":
        if R == "papel":print("Caso #{}: Bazinga!".format(x+1))
        if R == "Spock":print("Caso #{}: Bazinga!".format(x+1))
        if R == "tesoura":print("Caso #{}: Raj trapaceou!".format(x+1))
        if R == "pedra":print("Caso #{}: Raj trapaceou!".format(x+1))
