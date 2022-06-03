N,R = int(input()),0
for x in range(N):
    R+= 2.0
    R = 1.0/R
R += 1
print("{:.10f}".format(R))
