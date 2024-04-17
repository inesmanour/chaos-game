import matplotlib.pyplot as plt

# Données pour le graphique
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Création du graphique
plt.plot(x, y)
plt.title("Exemple de graphique Matplotlib")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Affichage du graphique
plt.show()
