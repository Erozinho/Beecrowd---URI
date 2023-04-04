n, m = map(int, input().split())
alturas = list(map(int, input().split()))
res, i = 0, 0
while i < n:
    res = res + abs(m - alturas[i])
    if alturas[i] == alturas[i+1]:
        i += 1
    else:
        alturas[i+1] = alturas[i+1] + (m - alturas[i])
    i += 1
print(res)
