# 2.1 — Positionnels vs mots-clés
def presenter(nom, age):
    return f"{nom} a {age} ans"


print(presenter("Sara", 22))
print(presenter(age=22, nom="Sara"))

# 2.2 — somme(*nombres)

def somme(*nombres):
    return sum(nombres)

print(somme(1, 2, 3))
print(somme(4, 5, 6, 7, 8))
print(somme())

# 2.3 — construire_fiche(**infos)

def construire_fiche(**infos):
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")

construire_fiche(
    nom="Ali",
    age=25,
    ville="Casablanca"
)

# 2.4 — Dépaquetage à l’appel

coordonnees = [3, 4]
infos = {"nom": "Sara", "age": 22}


def presenter(nom, age):
    return f"{nom} a {age} ans"


def distance_origine(x, y):
    return (x**2 + y**2) ** 0.5


print(distance_origine(*coordonnees))
print(presenter(**infos))

# 2.5 — Annotations de type

def addition(a: int, b: int) -> int:
    return a + b

print(addition(2, 3))
print(addition(2.5, 3.5))