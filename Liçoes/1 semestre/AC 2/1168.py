N1,N2,count = int(input()),int(input()),0
for i in range(N1, N2+1): 
  if i > 1: 
    for j in range(2, i): 
        if(i % j == 0): 
            break
    else: 
        print(i)
        count += 1
print("primos: {}".format(count))
