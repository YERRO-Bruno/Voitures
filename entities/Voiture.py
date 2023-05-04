from abc import abstractmethod

from entities.Energie import Energie


class Voiture:

    def __init__(self, nom: str, y: Energie):
        self._nom: str = nom
        self._energie = y

    @abstractmethod
    def allumer(self):
        pass

    def _get_nom(self):
        return self._nom

    def _set_nom(self, value: str):
        self._nom = value

    nom = property(_get_nom, _set_nom)
