while True:
    try:
        N = int(input())
        votos = list(map(int, input().split()))
        decider = 2/3 * N
        if sum(votos) >= decider: print("impeachment")
        else: print("acusacao arquivada")
    except EOFError:
        break
