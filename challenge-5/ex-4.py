from abc import ABC, abstractmethod
from typing import Callable


class Modele(ABC):

    @abstractmethod
    def entrainer(self, donnees):
        pass

    @abstractmethod
    def predire(self, entree):
        pass

class ModeleMoyenne(Modele):
    def entrainer(self, donnees):
        self._moyeen = sum(donnees) / len(donnees)

    def predire(self, entree):
        return self._moyeen

class ModeleLineaireSimple(Modele):
    def __init__(self, poids, biais):
        self.poids = poids
        self.biais = biais

    def entrainer(self, donnees):
        pass

    def predire(self, entree):
        return (self.poids * entree ) + self.biais

class Pipeline:
    def __init__(self, pretraitement: Callable[[list], list], modele: Modele):
        self.pretraitement = pretraitement
        self.modele = modele

    def executer(self, donnees, entree):
        donnees_preparers = self.pretraitement(donnees)
        self.modele.entrainer(donnees_preparers)

        return self.modele.predire(entree)


#  4.1 — Classe abstraite non instanciable
# modele  = Modele()

#  4.2 — ModeleMoyenne

donnees = [5, 8, 11]
modele = ModeleMoyenne()
modele.entrainer(donnees)
print(modele.predire(999))

#  4.3 — ModeleLineaireSimple

modele = ModeleLineaireSimple(poids=2, biais=1)
modele.entrainer(donnees=None)
print(modele.predire(5))

#  4.4 — Mini-challenge final : Pipeline par composition
def normaliser(donnees):
    maximum = max(donnees)
    return [d / maximum for d in donnees]

pipeline_moyenne = Pipeline(pretraitement=normaliser, modele=ModeleMoyenne())
pipeline_lineaire = Pipeline(pretraitement=normaliser, modele=ModeleLineaireSimple(2, 1))
donnees = [5, 8, 11]

for pipeline in [pipeline_moyenne, pipeline_lineaire]:
    resultat = pipeline.executer(donnees, entree=5)
    print(type(pipeline.modele).__name__, "->", resultat)