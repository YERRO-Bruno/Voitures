class Voiture:

    def __init__(self, nom : str):
        self._nom: str = nom

    def donne_moi_le_nom(self):
        return self._nom

    def _get_nom(self):
        return self._nom

    def _set_nom(self, value: str):
        if type(value) is not str:
            raise TypeError
        else:
            self._nom = value

    nom = property(_get_nom, _set_nom)
