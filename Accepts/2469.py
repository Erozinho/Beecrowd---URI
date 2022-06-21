from collections import Counter
NNOTAS = int(input())
NOTAS = list(map(int,input().split()))
NOTAS.sort(reverse=True)
c = Counter(NOTAS)
print(c.most_common(1)[0][0])
