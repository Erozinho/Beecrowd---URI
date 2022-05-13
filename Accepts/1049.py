A = str(input())
B = str(input())
C = str(input())
if A == "vertebrado" and B == "ave" and C == "carnivoro":
    ANIMAL = "aguia"
if A == "vertebrado" and B == "ave" and C == "onivoro":
    ANIMAL = "pomba"
if A == "vertebrado" and B == "mamifero" and C == "onivoro":
    ANIMAL = "homem"
if A == "vertebrado" and B == "mamifero" and C == "herbivoro":
    ANIMAL = "vaca"
if A == "invertebrado" and B == "inseto" and C == "hematofago":
    ANIMAL = "pulga"
if A == "invertebrado" and B == "inseto" and C == "herbivoro":
    ANIMAL = "lagarta"
if A == "invertebrado" and B == "anelideo" and C == "hematofago":
    ANIMAL = "sanguessuga"
if A == "invertebrado" and B == "anelideo" and C == "onivoro":
    ANIMAL = "minhoca"
print(ANIMAL)
