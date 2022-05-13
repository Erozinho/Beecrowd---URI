DIA,DATA_I = input().split()
DATA_I = int(DATA_I)
H1, M1, S1 = map(int,input().split(":"))
DIA,DATA_F = input().split()
DATA_F = int(DATA_F)
H2, M2, S2 = map(int,input().split(":"))
HRS = H2 - H1
MIN = M2 - M1
SEC = S2 - S1
DIAS = DATA_F - DATA_I
if SEC < 0:
    SEC = SEC + 60
    MIN = MIN - 1
if MIN < 0:
    MIN = MIN + 60
    HRS = HRS - 1
if HRS < 0:
    HRS = HRS + 24
    DIAS = DIAS - 1
print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(DIAS, HRS, MIN, SEC))
