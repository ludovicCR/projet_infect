#initiation variable
population = 11500000
nombre_infectes = 100
rencontre_jour = 10
PT = 0.01
PG = 0.05

#liste
liste_infectes = [nombre_infectes]
liste_jours = [1]

#Boucle pour calculer nombre infecté chaque jours !
for jour in range(2,366):
    if 30 <= jour <= 75:
        rencontre_jour = 3
    niag = liste_infectes[jour-2] * (1 - PG)
    nombre_infectes = niag + (population - niag) * rencontre_jour * niag / population * PT
    liste_infectes.append(nombre_infectes)
    liste_jours.append(jour)

#Affichage des résultats
while True:
    jour = int(input("Entrez un jour(Entre 1 et 365) ou 0 pour quitter : "))
    if jour == 0:
        break
