def welcome():
    name_visitor = input("Merci de contacter Thibault! Je peux avoir votre prénom?")
    print("Bienvenue chez Thibault " + name_visitor + ".")
    return

def shop_info():
    address = "148 Boulevard Masséna 75013 PARIS"
    schedule = "du Lundi au Samedi 10h-18h"
    print("Thibault se retrouve au " + address + ". La boutique est ouverte " + schedule + ".")
    other = input("Autre chose? [y/n]")
    if other == 'y':
        choose_category()
    else:
        print("Au revoir! Merci de nous avoir contacté.")
    return

def transfer_elliot():
    print("Parfait! Je vérifie le statut de votre commande.")
    return

def order_management():
    print("\nVous êtes au service de gestion des commandes.")
    client_name = input("Nom indiqué sur le bon de commande: ")
    order_number = input("Indiquez le numéro de commande: ")
    transfer_elliot()
    return

def transfer_christine():
    print("Merci pour vos détails. Nous vérifions votre commande et vous recontactons au plus vite.")
    return

def tracking_deliveries():
    print("Nous sommes désolés que vous ayez subi un souci avec votre commande.")
    client_name = input("Nom indiqué sur le bon de commande: ")
    order_number = input("Indiquez le numéro de commande: ")
    follow = input("Décrivez votre problème: ")
    transfer_christine()
    return

def transfer_raoul():
    suggestion_marketing = input("Dites-moi quel autre produit nous devrions proposer?")
    return

def service_marketing():
    print("Nous vous remercions pour votre suggestion et allons vous mettre en relation avec le service concerné.")
    transfer_raoul()
    return

def transfer_therese():
    other_info = input("De quoi aimeriez-vous nous informer?")
    return

def others():
    transfer_therese()
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
        # print("Horaires & Accès.")
        shop_info()
    elif choice == 2:
        # print("Gestion de commande.")
        order_management()
    elif choice == 3:
        # print("Suivi de livraison.")
        tracking_deliveries()
    elif choice == 4:
        # print("Suggestion de produit.")
        service_marketing()
    elif choice == 5:
        # print("Autre sujet.")
        others()
    else:
        print("Le choix n'est pas validé.")
        choose_category()
    return

welcome()
choose_category()
