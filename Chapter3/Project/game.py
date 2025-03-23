import random
"""
player = int(input("Que voulez-vous jouer? Pierre(1)/Ciseaux(2)/Papier(3)"))
pc = 1
print("Ordinateur: " + str(pc))
if player == 3:
    print("Le joueur gagne.")
elif player == 2:
    print("L'ordinateur gange.")
else:
    print("Les deux côtés sont à l'égalité.")
"""

# print(random.randint(1, 10))
player = int(input("Que voulez-vous jouer? Pierre(1)/Ciseaux(2)/Papier(3)"))
computer = random.randint(1, 3)
print("Ordinateur: " + str(computer))
if player == computer:
    print("Les deux côtés sont à égalité.")
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("Le joueur gagne.")
else:
    print("L'ordinateur gagne.")

