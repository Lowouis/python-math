# Fonction qui calcule le volume d'un
# parallelepiped avec sa longeur, largeur et hauteur
def volume():
    L = float(input("Saisir la longueur : "))
    l = float(input("Saisir la largeur : "))
    h = float(input("Saisir la hauteur : "))
    return L * l * h


# Convertir x secondes en minutes, heures & jours
def convert(second):
    minutes = second // 60
    hours = minutes // 60
    days = hours // 24
    return minutes, hours, days


# Inverser deux variables
def invert(a, b):
    temp = b
    b = a
    a = temp
    return a, b


# Permet de calculer un prix TTC
def taxe(price, taxes):
    return price * (1 + (taxes / 100))


# Fonction mystere
def mystery(a, b):
    c = a ** 2 + b
    b = a + b + c
    a = a * (a + 1)
    return (b - a) / 2


# give the average of speed by 2 parameters
def average_speed(km, t):
    return km // t


# convert km/h speed to m/s
def speed_convert(km):
    return (km * 10) / 3600


# exercice supp.
def calcP(a, b):
    if (((a / 100) + 1) * ((b / 100) + 1)) > 1:
        return print((((a / 100) + 1 * (b / 100) + 1) * 100) - 100, "% > Augmentation")
    return print((((a / 100) + 1 * (b / 100) + 1) * 100) - 100, "% < Diminution")


def piece_min():
    centimes_input = int(input("Entrez le nombre de pieces : "))
    cinquantC = centimes_input // 50
    reste = centimes_input % 50
    vingtC = reste // 20
    reste = vingtC % 20
    dixC = reste // 10
    reste = dixC % 10
    cinqC = reste // 5
    reste = cinqC % 5
    deuxC = reste // 2
    reste = deuxC % 2
    unC = reste // 1
    somme = (cinquantC*50) + (vingtC*20) + (dixC*10) + (cinqC*5) + (deuxC*2) + (unC)
    print(somme==centimes_input)
    return "Piece de 50 : "+str(cinquantC)+" > Piece de 20 : "+str(vingtC)+" > Piece de 10 : "+str(dixC)+" > Piece de 5 : "+str(cinqC)+" > Piece de 2 : "+str(deuxC)+" > Piece de 1 : "+str(unC)

print(piece_min())