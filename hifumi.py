# Librairies
import random

# Données
scoreUser       = 0
scoreComputer   = 0
options = ["Pierre", "Feuille", "Ciseaux"]

while True :
    # L'utilisateur commence la partie
    choiceUser = input("- Pierre, Feuille ou Ciseaux ? ")

    # Au tour de la machine
    randomOption = random.randrange(0,3)
    choiceComputer = options[randomOption]


    # Posibilité avec la Pierre
    if choiceUser == "Pierre" and choiceComputer == "Pierre":
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Match nul")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")

    elif choiceUser == "Pierre" and choiceComputer == "Feuille":
        scoreComputer += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- La machine a gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")

    elif choiceUser == "Pierre" and choiceComputer == "Ciseaux":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")




    # Posibilité avec la Feuille
    elif choiceUser == "Feuille" and choiceComputer == "Feuille":
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Match nul")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer))

    elif choiceUser == "Feuille" and choiceComputer == "Pierre":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")

    elif choiceUser == "Pierre" and choiceComputer == "Ciseaux":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")




    # Posibilité avec la Ciseau
    elif choiceUser == "Ciseaux" and choiceComputer == "Ciseaux":
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Match nul")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")

    elif choiceUser == "Ciseaux" and choiceComputer == "Pierre":
        scoreComputer += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez perdu")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")

    elif choiceUser == "Ciseaux" and choiceComputer == "Feuille":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")

    else:
        print("- " + choiceUser + " est une réponse incorrecte")

    if (scoreUser == 3 or scoreComputer == 3 ):
        print("fin")
        break
