# 1.1 — Création d’un livre
class LivreException(Exception):
    pass

class Livre:
    def __init__(self, titre: str, auteur: str, disponible: bool = True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def __str__(self) -> str:
        return f"{self.titre} de {self.auteur} -- {'disponible' if self.disponible else 'non disponible'}"

class Adherent:
    def __init__(self, nom: str):
        self.nom = nom
        self.liste_livres = []

    def emprunter_livre(self, liver: Livre):
        try:
            if not liver.disponible:
                raise LivreException(f'le livre "{liver.titre}" n’est pas disponible.')
            self.liste_livres.append(liver)
            liver.emprunter()
        except LivreException as message:
            print(f'Erreur : {message}')

    def rendre_livre(self, liver: Livre):
        try:
            if liver.disponible:
                raise LivreException(f'le livre "{liver.titre}" est déja disponible.')
            liver.rendre()
            self.liste_livres.remove(liver)
        except LivreException as message:
            print(f'Erreur : {message}')

    def nombre_livres_empruntes(self):
        print(len(self.liste_livres))

livre = Livre("Dune", "Frank Herbert")
print(livre)

# 1.2 — Emprunt réussi

#  1.3 — Tentative d’emprunt d’un livre indisponible

ali = Adherent("Ali")
sara = Adherent("Sara")

ali.emprunter_livre(livre)
# sara.emprunter_livre(livre)

#  1.4 — Retour d’un livre

ali.rendre_livre(livre)
print(livre)

ali.nombre_livres_empruntes()
