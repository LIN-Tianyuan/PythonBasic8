"""
score_str = input("Veuillez entrer votre score: ")
print(score_str)
score = int(score_str)
"""
score = int(input("Veuillez entrer votre score: "))
if score >= 60:
    print("Vous avez passé.")
    if score >= 80:
        print("Vous êtes très bon.")
    else:
        print("Vous êtes juste dans la moyenne.")
else:
    print("Echec à la réussite.")
    if score < 30:
        print("De très mauvaises notes.")
    else:
        print("Il faut continuer à faire du bon travail.")