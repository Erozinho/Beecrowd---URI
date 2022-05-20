import math
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
print("{:.4f}".format(math.sqrt(((x2 - x1)*(x2 - x1)) + ((y2 - y1)) *(y2 - y1))))

# Codigo velho:

#import math
#linha1 = input().split(" ")
#linha2 = input().split(" ")
#x1,y1 = linha1
#x2,y2 = linha2
#raiz = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
#print("{:.4f}".format(raiz))
