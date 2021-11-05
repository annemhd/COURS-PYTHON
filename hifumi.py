# Librairies
import random

# Données
scoreUser       = 0
scoreComputer   = 0
options         = ["Pierre", "Feuille", "Ciseaux"]
separator       = "-------------------------------------------------------------------"

# La partie continue jusqu'à ce qu'un joueur atteint le score de 3
while True :
    # L'utilisateur commence la partie
    choiceUser = input("- Pierre, Feuille ou Ciseaux ? ")

    # Au tour de la machine
    randomOption = random.randrange(0,3)
    choiceComputer = options[randomOption]


    # Posibilités avec la Pierre
    if choiceUser == "Pierre" and choiceComputer == "Pierre":
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Match nul")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)

    elif choiceUser == "Pierre" and choiceComputer == "Feuille":
        scoreComputer += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- La machine a gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)

    elif choiceUser == "Pierre" and choiceComputer == "Ciseaux":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)



    # Posibilités avec la Feuille
    elif choiceUser == "Feuille" and choiceComputer == "Feuille":
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Match nul")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer))
        print(separator)

    elif choiceUser == "Feuille" and choiceComputer == "Pierre":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)

    elif choiceUser == "Pierre" and choiceComputer == "Ciseaux":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)



    # Posibilités avec la Ciseau
    elif choiceUser == "Ciseaux" and choiceComputer == "Ciseaux":
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Match nul")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)

    elif choiceUser == "Ciseaux" and choiceComputer == "Pierre":
        scoreComputer += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez perdu")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)

    elif choiceUser == "Ciseaux" and choiceComputer == "Feuille":
        scoreUser += 1
        print("- Vous avez choisi " + choiceUser)
        print("- La machine à choisi " + choiceComputer)
        print("- Vous avez gagné")
        print("Vous " + str(scoreUser) + " - " + str(scoreComputer) + " Ordinateur")
        print(separator)


    # Si la réponse est au mauvais format (Pas de majuscule au début du mot. ex: pierre = incorrect)
    else:
        print("- " + choiceUser + " est une réponse incorrecte")
        print(separator)


    # Fin de la partie, quand un des deux joueurs à atteint le scrore de 3
    if (scoreUser == 3 or scoreComputer == 3 ):

        # Message à afficher pour le gagnat ou le perdant
        if (scoreComputer == 3):
            print("VOUS AVEZ PERDU...")
        else:
            print("FÉLICITATION, VOUS AVEZ GAGNÉ !")

        print("- Fin de la partie")
        print("- Pour recommencer, relancer la cmd : ")
        print("- py hifumi.py")
        print("- ou")
        print("- python3 hifumi.py")
        break
