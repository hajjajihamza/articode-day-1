# 1.1 — saluer(nom)

def saluer(nom):
    print(f"Bonjour {nom} !")


saluer("Ali")

# 1.2 — puissance(base, exposant=2)

def puissance(base, exposant=2):
    return base ** exposant


print(puissance(3))
print(puissance(2, 5))


# 1.3 — Fonction sans return

def afficher_message(message):
    print(message)

resultat = afficher_message("Traitement termine")

print(resultat)

# 1.4 — diviser_avec_reste(a, b) — retour multiple

def diviser_avec_reste(a, b):
    quotient = a // b
    reste = a % b

    return quotient, reste


quotient, reste = diviser_avec_reste(17, 5)

print("quotient ->", quotient)
print("reste ->", reste)