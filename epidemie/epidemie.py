import csv

import matplotlib.pyplot as plt

susceptibles = 100000
malades = 1
gueris = 0
morts = 0

p_contamination = 0.000005  # probabilité de contamination par jour
p_guerison = 0.1  # probabilité de guérison par jour
p_deces = 0.0001  # probabilité de deces par jour

courbe_infection = []
duree = 50  # nombre de jours consideres
for i in range(duree):

    # modele de base
    infections = p_contamination * malades * susceptibles
    guerisons = p_guerison * malades
    deces = p_deces * malades

    # pour éviter les nombres négatifs dus à la méthode d'Euler (à ajouter ensuite)
    infections = min(infections, susceptibles)
    deces = min(deces, malades)
    guerisons = min(guerisons, malades)

    susceptibles = susceptibles - infections
    malades = malades + infections - deces - guerisons
    morts = morts + deces
    gueris = gueris + guerisons
    courbe_infection.append(infections)

# on imprime le nombre de personne appartenant a chaque categorie
print("Susceptibles:", susceptibles)
print("Malades:", malades)
print("Guéris:", gueris)
print("Morts:", morts)

# on fait un graphique du nombre d'infections
plt.plot(courbe_infection, "-")
plt.xlabel("jours")
plt.ylabel("nombres d'infections")
plt.show()

# on affiche la vraie courbe
cascumul = []
ncas = []
date = []
with open("covid_vd.csv") as covid_file:
    reader = csv.DictReader(covid_file)
    for row in reader:
        date.append(row["Date"])
        diff = float(row["VD_diff"] or 0)
        ncas.append(diff)
plt.plot(ncas)
plt.show()
