from entities.Energie import Energie
from entities.Voiture import Voiture
from entities.VoitureElectrique import VoitureElectrique


def print_hi(name):
    ma_deuxieme_voiture: Voiture = Voiture('2', Energie.ESSENCE)
    ma_voiture : VoitureElectrique = VoitureElectrique('2')


    ma_voiture_custom : Voiture = VoitureElectrique('2')
    ma_voiture_custom: VoitureElectrique = Voiture('2',Energie.ELECTRIQUE)

    print(type(ma_voiture_custom))


    ma_deuxieme_voiture.nom = 50
    print(ma_deuxieme_voiture.nom)


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
