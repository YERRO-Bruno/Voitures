from entities.Energie import Energie
from entities.Voiture import Voiture


class VoitureElectrique(Voiture):

    def __init__(self, nom: str, capacite_batterie: int):
        Voiture.__init__(self, nom, Energie.ELECTRIQUE)
        self._capacite_batterie = capacite_batterie

    def allumer(self):
        print("je suis allumé !")
