NUM_CHA,c = int(input()),0
PALPITES = list(map(int,input().split()))
for x in range(5):
    if PALPITES[x] == NUM_CHA:
        c += 1
print(c)
