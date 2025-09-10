# students grade tracker
# Ask the user to enter student names and their grades.
# Allow them to:
# Add a student with a grade
# Update a grade
# Display all students and their grades
# Example: { "Alice": 15, "Bob": 12 }


# Phase 1: Structure de base (Commence par ça)
# 1. Planification des données

# Format: {"Alice": 15, "Bob": 12, "Charlie": 18}
# Un dictionnaire où clé = nom étudiant, valeur = note

# 2. Menu principal
# Crée une boucle avec options :
# 1. Add student
# 2. Update grade
# 3. Display all students
# 4. Exit
# 3. Structure de base
# pythondef main():
#     students = {}  # Ton dictionnaire d'étudiants
    
#     while True:
        # afficher menu
        # demander choix utilisateur
#         # appeler la bonne fonction
# 🛠️ Phase 2: Fonctions individuelles
# 4. Fonction add_student()

# Demander le nom de l'étudiant
# Demander sa note
# Vérifier si l'étudiant existe déjà
# L'ajouter au dictionnaire

# 5. Fonction update_grade()

# Demander le nom de l'étudiant
# Vérifier s'il existe
# Demander la nouvelle note
# Mettre à jour le dictionnaire

# 6. Fonction display_students()

# Parcourir le dictionnaire avec .items()
# Afficher nom et note
# Gérer le cas dictionnaire vide

# 🎯 Phase 3: Améliorations
# 7. Validation

# Notes entre 0 et 20 (ou ton système)
# Noms non vides
# Gestion casse (Alice = alice ?)

# 8. Fonctionnalités bonus

# Calculer la moyenne générale
# Trouver meilleur/pire élève
# Supprimer un étudiant

# 🚀 Questions pour démarrer :

# Système de notation : Sur 20 ? Sur 100 ? Lettres (A,B,C) ?
# Gestion des doublons : Si on ajoute "Alice" deux fois, que faire ?

# Remplacer la note ?
# Refuser l'ajout ?


# Casse des noms : "Alice" et "alice" sont-ils différents ?

# 💡 Ordre recommandé d'implémentation :
# Étape 1: Menu + display_students()
# pythonstudents = {"Alice": 15, "Bob": 12}  # Test avec données
# # Juste afficher pour commencer
# Étape 2: add_student()
# python# Ajouter sans validation d'abord
# Étape 3: update_grade()
# python# Vérifier si étudiant existe
# Étape 4: Validation et gestion d'erreurs
# 🔍 Points clés à retenir :

# Dictionnaires : students[nom] = note pour ajouter/modifier
# Vérification existence : if nom in students:
# Parcours : for nom, note in students.items():
# Dictionnaire vide : if not students:





# def display_students(students):
#     if not students:  # Si dictionnaire vide
#         print("Aucun étudiant enregistré")
#     else:
#         print("Liste des étudiants:")
#         for nom, note in students.items():
#             print(f"• {nom}: {note}/20")


def main():
    pass  # TODO: implement main logic


if __name__ == "__main__":
    main()