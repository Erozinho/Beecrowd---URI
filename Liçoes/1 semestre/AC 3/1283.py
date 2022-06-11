MEDIA,M = [],0
while True:
    NUM = int(input())
    if NUM < 0:break
    else:MEDIA.append(NUM)
print("MEDIA: {:.2f}".format(sum(MEDIA)/len(MEDIA)))
for i in range(len(MEDIA)):
    if MEDIA[i] < sum(MEDIA)/len(MEDIA):print(MEDIA[i])
