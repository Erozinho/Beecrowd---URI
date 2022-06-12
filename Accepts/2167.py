N,M = int(input()),0
RPM = list(map(int,input().split()))
for x in range(1, N):
    if RPM[x-1] > RPM[x]:
        M = x + 1
        break
print(M)
