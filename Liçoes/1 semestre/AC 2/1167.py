from calendar import isleap
A1,A2,B = int(input()),int(input()),0
for x in range(A1, A2+1):
    if isleap(x):
        print(x)
        B +=1
print("bissextos: {}".format(B))
