from math import sqrt
N = int(input())
print("{:.1f}".format((1 / sqrt(5)) * pow(((1 + sqrt(5)) / 2), N) - ( 1 / sqrt(5)) * pow((( 1 - sqrt(5)) / 2), N)))
