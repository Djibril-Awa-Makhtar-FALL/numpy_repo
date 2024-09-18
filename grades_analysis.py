# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 00:22:50 2024

@author: Djibril Awa Makhtar FALL

Point de contrôle Python Numpy
"""

# 1) Créez un nouveau fichier appelé « grades_analysis.py »

# 2) Importez la bibliothèque numpy et créez le tableau « notes » comme spécifié ci-dessus. 

import numpy as np

# Créez du tableau « grades »

notes = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

""" 3) Utilisez les fonctions numpy pour calculer la moyenne, la médiane
et l’écart type des notes."""

# Calcul de la moyenne des notes 
    
moyenne = np.mean(notes)

# Affichage de la moyenne des notes 
    
print(f"La moyenne des notes est : {moyenne}")

# Calcul de la médiane

mediane = np.median(notes)

print(f"La médiane des notes est : {mediane}")

# Calcul de l'écart type des notes 
    
ecart_type = np.std(notes)

# Affichage de l'écart type des notes

print(f"L'écart type des notes est : {ecart_type}")

# 4) Utilisez la fonction numpy pour trouver le maximum et le minimum des notes.

# Trouver le maximum des notes 

maximum = np.max(notes)

# Affichage du maiximum des notes

print(f"Le maximum des notes est : {maximum}")

# Trouver le minimum des notes 

minimum = np.min(notes)

# Affichage du minimum des notes

print(f"Le minimum des notes est : {minimum}")

# 5) Utilisez la fonction numpy pour trier les notes par ordre croissant.

tri_note = np.sort(notes)

# Affichage des notes triées par ordre décroissant

print(f"trier les notes par ordre décroissant : {tri_note}")

"""6) Utilisez la fonction numpy pour trouver l'index de la note 
la plus élevée dans le tableau."""

index_plus_eleve = np.argmax(notes)

# Affichage de l'index de la note la plus élevée 

print(f"L'index de la note la plus élevée est : {index_plus_eleve}")

"""7) Utilisez la fonction numpy pour compter le nombre d'étudiants ayant obtenu
 un score supérieur à 90."""
 
score = np.sum(np.array(notes) > 90)

print(f"Le nombre d'étudiant ayant obtenu un score supérieur à 90 est de : {score}")

""" 8) Utilisez la fonction numpy pour calculer le pourcentage d'étudiants ayant
 obtenu un score supérieur à 90."""
 
# Calculons d'abord le nombre total des étudiants :

nmbre_total_etudiant = len(notes)

pourcentage = (score /  nmbre_total_etudiant) * 100 

print(f"Le pourcentage d'étudiants ayant obtenu un score supérieur à 90 est de : {pourcentage}")

""" 9) Utilisez la fonction numpy pour calculer le pourcentage d'étudiants ayant obtenu
un score inférieur à 75."""

score_inferieur = np.sum(np.array(notes) < 75)

pourcentage_inferieur = (score_inferieur / nmbre_total_etudiant) * 100

print(f"Le pourcentage d'étudiants ayant obtenu un score inférieur à 75 est de : {pourcentage_inferieur}")

"""10) Utilisez la fonction numpy pour extraire toutes les notes supérieures à 90
 et les placer dans un nouveau tableau appelé « high_performers ». """
 
high_performers = notes[notes > 90]

print(f"Les notes supérieur à 90 sont : {high_performers}")
 
# 11) Créez un nouveau tableau appelé « passing_grades » qui contient toutes les notes supérieures à 75.

passing_grades = notes[notes > 75]

print(f"Les notes supérieures à 75 sont : {passing_grades}")

# 12) Imprimez le résultat de toutes les étapes ci-dessus.


