from abc import ABC, abstractmethod


class Vehicule(ABC):
    def __init__(self, marque:str, immatriculation:str):
        self._marque = marque
        self._immatriculation = immatriculation

    @abstractmethod
    def tarif_journalier(self):
        pass

    @property
    def marque(self):
        print(self._marque)
        return self._marque

class Voiture(Vehicule):
    def __init__(self, marque:str, immatriculation:str, nombre_places: int):
        super().__init__(marque, immatriculation)
        self.nombre_places = nombre_places

    def tarif_journalier(self):
        print(20 + (5 * self.nombre_places))
        return 20 + (5 * self.nombre_places)

    def __str__(self) -> str:
        return f"{self._marque} ({self._immatriculation}) -- {self.nombre_places} place -- {self.tarif_journalier()}/jour"
class Moto(Vehicule):
    def __init__(self, marque:str, immatriculation:str, cylindree: int):
        super().__init__(marque, immatriculation)
        self.cylindree = cylindree

    def tarif_journalier(self):
        print(20 + (5 * self.cylindree))
        return 20 + (5 * self.cylindree)

class Camion(Vehicule):
    def __init__(self, marque:str, immatriculation:str, charge_utile: int):
        super().__init__(marque, immatriculation)
        self.charge_utile = charge_utile

    def tarif_journalier(self):
        print(20 + (5 * self.charge_utile))
        return 20 + (5 * self.charge_utile)

# 3.1 — Construction via super()
voiture = Voiture("Renault", "123-A-45", nombre_places=5)
voiture.marque
voiture.tarif_journalier()

#  3.2 — Tarifs différents selon le type
moto = Moto("Yamaha", "987-B-65", cylindree=600)
camion = Camion("Volvo", "456-C-78", charge_utile=3000)
moto.tarif_journalier()
camion.tarif_journalier()

#  3.3 — Polymorphisme sur la flotte

flotte = [
    Voiture("Renault", "123-A-45", nombre_places=5),
    Moto("Yamaha", "987-B-65", cylindree=600),
    Camion("Volvo", "456-C-78", charge_utile=3000),
]
for v in flotte:
    print(v.marque, "->", v.tarif_journalier())

# 3.4 — Affichage personnalisé (__str__)
voiture = Voiture("Renault", "123-A-45", nombre_places=5)
print(voiture)