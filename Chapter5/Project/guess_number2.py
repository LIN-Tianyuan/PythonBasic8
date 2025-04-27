import random
computer = random.randint(1, 100)
player = None
print(computer)
count = 0
while count < 5:
    player = int(input("Veuillez entrer un nombre: "))
    count = count + 1
    if player > computer:
        print("Plus grand.")
    elif player < computer:
        print("Plus petit.")
    else:
        print("Bien deviné " + str(count) + " fois.")
        break
if count == 5 and player != computer:
    print("Game over, vous avez échoué.")