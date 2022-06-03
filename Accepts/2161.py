N,R = int(input()),0
for x in range(N):
    R+= 6
    R = 1/R
R += 3
print("{:.10f}".format(R))
