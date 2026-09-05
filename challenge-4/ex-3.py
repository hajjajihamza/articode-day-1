# 3.1 — Variable locale vs globale

compteur = 0
def incrementer_local():
    compteur = compteur + 1 # sans "global"
    return compteur
# incrementer_local()


#  3.2 — Modification avec global

compteur = 0
def incrementer():
    global compteur
    compteur += 1
incrementer()
incrementer()
incrementer()
print(compteur)

# 3.3 — Fonction imbriquée & nonlocal

def creer_compteur():
    valeur = 0

    def incrementer():
        nonlocal valeur
        valeur += 1
        return valeur

    return incrementer


compteur1 = creer_compteur()

print(compteur1())
print(compteur1())
print(compteur1())

# 3.4 — Fonction passée en argument

def additionner(a, b):
    return a + b


def multiplier(a, b):
    return a * b


def appliquer_operation(a, b, operation):
    return operation(a, b)


print(appliquer_operation(4, 5, additionner))
print(appliquer_operation(4, 5, multiplier))

# 3.5 — Closure : creer_multiplicateur(facteur)

def creer_multiplicateur(facteur):

    def multiplier(nombre):
        return nombre * facteur

    return multiplier


fois_trois = creer_multiplicateur(3)
fois_dix = creer_multiplicateur(10)

print(fois_trois(7))
print(fois_dix(7))