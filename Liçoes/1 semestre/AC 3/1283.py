MEDIA,M = [],0
while True:
    NUM = int(input())
    if NUM < 0:break
    else:
        MEDIA.append(NUM)
for x in range(len(MEDIA)):
    M += MEDIA[x]
print("MEDIA: {:.2f}".format(M/len(MEDIA)))
for i in range(len(MEDIA)):
    if MEDIA[i] < M/len(MEDIA):print(MEDIA[i])
