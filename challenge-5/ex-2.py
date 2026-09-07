class CompteBancaire:
    nom_banque = 'BanquePyDiag'
    count_comptes = 0

    def __init__(self, nom: str, solde_initial: float):
        self._nom = nom
        self.__solde = solde_initial
        CompteBancaire.count_comptes += 1

    @property
    def solde(self):
        print(self.__solde)
        return self.__solde

    def deposer(self, montant: float):
        try:
            if montant < 0:
                raise ValueError(f' le montant du depot doit etre positif ({montant}).')
            self.__solde += montant
        except ValueError as ms:
            print(ms)

    def retirer(self, montant: float):
        try:
            if montant > self.__solde:
                raise ValueError(f'fonds insuffisants (solde : {self.__solde}, retrait demande : {montant}).')
            self.__solde -= montant
        except ValueError as m:
            print(m)

    @classmethod
    def nombre_comptes(cls):
        print(cls.count_comptes)

    @staticmethod
    def convertir_devise(montant:float, taux:float):
        print(montant * taux)


# 2.1 — Solde en lecture seule
#
# compte = CompteBancaire("Ali", solde_initial=100)
# compte.solde
# # compte.solde = 5000
#
# # 2.2 — Dépôt et retrait valides
# compte.deposer(50)
# compte.retirer(30)
# compte.solde
#
# # 2.3 — Opérations invalides
#
# compte.deposer(-20)
# compte.retirer(500)
#
# #  2.4 — Attribut de classe vs attribut d’instance
#
# c1 = CompteBancaire("Ali", 100)
# c2 = CompteBancaire("Sara", 200)
# print(c1.nom_banque, c2.nom_banque)
# print(c1.solde, c2.solde)

#  2.5 — classmethod & staticmethod

c1 = CompteBancaire("Ali", 100)
c2 = CompteBancaire("Sara", 200)
c3 = CompteBancaire("Lina", 0)
CompteBancaire.nombre_comptes()
CompteBancaire.convertir_devise(100, taux=10.5)