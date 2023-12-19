import math
import random

# Fonction d'affichage des statistiques
def AfficherStats(stats):
    print("Statistiques du joueur :")
    print("Attaque :", stats[0])
    print("Défense :", stats[1])
    print("HP :", stats[2], "/", stats[3])
    print("Niveau :", stats[4])
    print("XP :", stats[5])
    print("Points de stats :", stats[6])

# Fonction pour soigner le joueur
def Soigner(stats):
    moitieHP = math.ceil(stats[3] / 2.0)
    stats[2] = min(stats[3], stats[2] + moitieHP)
    return stats

# Fonction pour calculer le coût du prochain niveau
def CoutProchainNiveau(niveauActuel):
    if niveauActuel == 0:
        return 1
    elif niveauActuel == 1:
        return 2
    else:
        return CoutProchainNiveau(niveauActuel - 1) + CoutProchainNiveau(niveauActuel - 2)

# Fonction pour vérifier si le joueur peut monter de niveau
def PeutMonterDeNiveau(niveauActuel, experience):
    return experience >= CoutProchainNiveau(niveauActuel)

# Fonction pour monter de niveau et attribuer des points de stats
def MonterNiveau(stats):
    if PeutMonterDeNiveau(stats[4], stats[5]):
        stats[5] -= CoutProchainNiveau(stats[4])
        stats[6] += stats[4]
        print("Vous avez gagné des points de stats !")
        print("Vous avez", stats[6], "points de stats à dépenser.")
        print("Comment voulez-vous les dépenser ?")
        print("1. Dépenser 1 point pour gagner 1 attaque")
        print("2. Dépenser 1 point pour gagner 1 défense")
        print("3. Dépenser 1 point pour gagner 2 HPMax (et 1 HP)")

        while stats[6] > 0:
            choix = int(input("Saisissez votre choix : "))
            if choix == 1:
                stats[0] += 1
            elif choix == 2:
                stats[1] += 1
            elif choix == 3:
                stats[2] += 2
            stats[6] -= 1
            AfficherStats(stats)
            print("Il vous reste", stats[6], "points de stats.")
    else:
        print("Vous n'avez pas assez d'XP pour monter de niveau.")

    return stats

# Fonction pour chasser un ennemi
def Chasser(stats, ennemi, tour):
    ennemi = GenererEnnemi(ennemi, tour)
    stats = Combattre(stats, ennemi)

    if stats[2] > 0:
        stats[5] += tour

    return stats

# Fonction pour générer un ennemi
def GenererEnnemi(ennemi, tour):
    ennemi[0] = 1
    ennemi[1] = 0
    ennemi[2] = 1

    if tour % 10 == 0:
        ennemi[0] += random.randint(1, tour)
        ennemi[1] += random.randint(1, tour)
        ennemi[2] += random.randint(1, tour)
    else:
        ennemi[0] += random.randint(1, tour)
        ennemi[1] += random.randint(1, tour)
        ennemi[2] += random.randint(1, tour)

    return ennemi
