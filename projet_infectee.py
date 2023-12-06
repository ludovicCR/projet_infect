
population = 11500000
nombre_infectes = 100
rencontre_jour = 10
PT = 0.01
PG = 0.05

#liste
liste_infectes = [nombre_infectes]
liste_jours = [1]
liste_nouvelles_infections = [nombre_infectes]

#Boucle pour calculer nombre infecté chaque jours !
for jour in range(0,365):
    if 30 <= jour <= 75:
        rencontre_jour = 3
    else:
        rencontre_jour = 10
    niag = liste_infectes[jour] * (1 - PG)
    nombre_infectes = niag + (population - niag) * rencontre_jour * niag / population * PT

    liste_infectes.append(nombre_infectes)
    liste_jours.append(jour)

    liste_nouvelles_infections.append(nombre_infectes - liste_infectes[jour])

#Calcul nombre moyen de personne infecté par jour.
nombre_moyen_infectes = sum(liste_infectes) / len(liste_infectes)

#Affichage des résultats
while True:
    jour = int(input("Entrez un jour(Entre 1 et 365) ou 0 pour quitter : "))
    if jour == 0:
        break
    elif jour < 1 or jour > 365:
        print("Jour invalide, veuillez entrez un nombre entre 1 et 365")
    else: 
        print("Jour",jour,":",round(liste_infectes[jour-1],2), "personnes infectées")
print("Le nombre moyen de personnes infectés par jour sur l'ensemble de l'année est de :",round(nombre_moyen_infectes,2))