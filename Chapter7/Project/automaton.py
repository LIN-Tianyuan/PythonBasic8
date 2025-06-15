def welcome():
    name_visitor = input("Merci de contacter Thibault! Je peux avoir votre prénom?")
    print("Bienvenue chez Thibault " + name_visitor + ".")
    return

def choose_category():
    print("*** Menu général Thibault ***\n"
          "[1] Horaires & Accès \n"
          "[2] Gestion de commande \n"
          "[3] Suivi de livraison \n"
          "[4] Suggestion de produit \n"
          "[5] Autre sujet")
    choice = int(input("Choisissez une des catégories en tapant un chiffre entre 1 et 5: "))
    if choice == 1:
        print("Horaires & Accès.")
    elif choice == 2:
        print("Gestion de commande.")
    elif choice == 3:
        print("Suivi de livraison.")
    elif choice == 4:
        print("Suggestion de produit.")
    elif choice == 5:
        print("Autre sujet.")
    else:
        print("Le choix n'est pas validé.")
        choose_category()

welcome()
choose_category()