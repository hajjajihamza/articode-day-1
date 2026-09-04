#  3.1 — ecrire_liste_courses(chemin, articles) (mode w)

def ecrire_liste_courses(chemin, articles):
    try:
        with open(chemin,'w', encoding='utf-8') as ficher:
            ficher.write("\n".join(articles))
    except OSError as message:
        print(message)

# articles = ["pommes", "lait", "pain"]
# ecrire_liste_courses("courses.txt", articles)

# 3.2 — ajouter_article(chemin, article) (mode a)
def ajouter_article(chemin, article):
    try:
        with open(chemin, 'a', encoding='utf-8') as ficher:
            ficher.write("\n" + article)
    except OSError:
        raise

# ajouter_article("courses.txt", "oeufs")


from pathlib import Path
# 3.3 — lire_fichier(chemin) avec with et readlines()
def lire_fichier(chemin):
    ficher_chemin = Path(chemin)
    with ficher_chemin.open('r', encoding='utf-8') as ficher:
        print(ficher.readlines())

# lire_fichier("courses.txt")

#  3.4 — compter_lignes(chemin) avec parcours ligne par ligne

def compter_lignes(chemin):
    ficher_chemin = Path(chemin)
    with ficher_chemin.open('r', encoding="utf-8") as ficher:
        print(len(ficher.readlines()))

# compter_lignes("courses.txt")


# 3.5 — Modes d’ouverture

# modes_a_identifier = ["r", "w", "a", "x", "rb", "r+"]

