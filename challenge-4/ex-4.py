# 4.1 — lambda simple

carre = lambda x: x ** 2
carre(6)

# 4.2 — map() avec lambda
nombres = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, nombres)))

#  4.3 — filter() avec lambda

nombres = [3, 12, 7, 25, 8, 19, 2]
print(list(filter(lambda x: x % 2 == 0, nombres)))

#  4.4 — Fonction récursive factorielle(n)

def factorielle(n):
    if n < 1:
        return 1
    return n * factorielle(n -1)

print(factorielle(0))
print(factorielle(5))

# 4.5 — Mini-challenge final : pipeline de traitement

def pipeline(*fonctions):
    def executer(valeur):
        resultat = valeur
        for f in fonctions:
            resultat = f(resultat)
        return resultat
    return executer

doubler = lambda x: x * 2
ajouter_un = lambda x: x + 1

traitement = pipeline(doubler, ajouter_un, doubler)
print(traitement(5))

notes = [8, 15, 3, 20, 11, 6]
notes_admises = list(filter(lambda n: n >= 10, notes))
notes_sur_100 = list(map(lambda n: n * 5, notes_admises))

print(notes_admises)
print(notes_sur_100)