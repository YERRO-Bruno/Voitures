from entities.Voiture import Voiture


def print_hi(name):

    # maVoiture est instance de Voiture
    # 'une version'
    ma_voiture : Voiture = Voiture(name)

    ma_deuxieme_voiture: Voiture = Voiture('2')

    mon_nom : str = ma_voiture.donne_moi_le_nom()
    ma_deuxieme_voiture.nom = 50
    print(ma_deuxieme_voiture.nom)

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
