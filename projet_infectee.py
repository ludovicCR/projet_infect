#Initiation
POPULATION = 11500000
nombre_infectes = 100
rencontre_jour = 10
PT = 0.01
PG = 0.05

#liste
liste_infectes = [nombre_infectes]
liste_jours = [1]
liste_nouvelles_infections = [nombre_infectes]

#Fonction avec Boucle pour calculer nombre infecté chaque jours !
def simuler_propagation():
    for jour in range(0,730): #Ajout de 2 ans.
        if jour >= 365: #Ajout du vaccin
            rencontre_jour = 4
        if 30 <= jour <= 75:
            rencontre_jour = 3
        else:
            rencontre_jour = 10

        niag = liste_infectes[jour] * (1 - PG)
        nombre_infectes = niag + (POPULATION - niag) * rencontre_jour * niag / POPULATION * PT

        liste_infectes.append(nombre_infectes)
        liste_jours.append(jour)
        liste_nouvelles_infections.append(nombre_infectes - liste_infectes[jour])

#Fonction du pic maximum :
def trouver_pic_max():
    indice_max = liste_infectes.index((liste_infectes))
    jour_pic_maximum = liste_jours[indice_max]
    return jour_pic_maximum

# Fonction pour calculer le nombre moyen de personnes infectées par jour
def calculer_nombre_moyen_infectes():
    return round(sum(liste_infectes) / len(liste_infectes), 2)

# Fonction pour calculer le nombre moyen de nouvelles infections par jour
def calculer_nombre_moyen_nouvelles_infections():
    return round(sum(liste_nouvelles_infections) / len(liste_nouvelles_infections), 2)

# Fonction pour afficher le nombre de personnes infectées pour un jour donné
def afficher_nombre_infectes(jour):
    print(f"Jour {jour}: {round(liste_infectes[jour-1])} personnes infectées")

# Fonction pour afficher le nombre moyen de personnes infectées par jour sur l'ensemble de l'année
def afficher_nombre_moyen():
    print(f"Le nombre moyen de personnes infectées par jour sur l'ensemble de l'année est de : {round(calculer_nombre_moyen_infectes())}")
    print(f"Le nombre moyen de nouvelles infections par jour sur l'ensemble de l'année est de : {round(calculer_nombre_moyen_nouvelles_infections())}")

#Affichage des résultats
while True:
    jour = int(input("Entrez un jour(Entre 1 et 730) ou 0 pour quitter : "))
    simuler_propagation()
    jour_pic_max = trouver_pic_max()
    if jour == 0:
        break
    elif jour < 1 or jour > 730:
        print("Jour invalide, veuillez entrez un nombre entre 1 et 365")
    else: 
        afficher_nombre_infectes(jour)
print(f"Le jour du pic maximum de personnes infectées est le jour :{jour_pic_max}")
afficher_nombre_moyen()
