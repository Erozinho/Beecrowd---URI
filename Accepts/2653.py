J = []
while True:
    try:
        J.append(input())
    except EOFError:
        break
J = set(J)
print(len(J))
