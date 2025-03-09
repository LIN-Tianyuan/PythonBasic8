# if condition:
#    action
# elif condition:
#    action
# else:
#    action

number_a = input("Veuillez entrer un nombre a: ")
# print(number_a)
a = int(number_a)
if a > 0:
    print("Nombre a est positif.")
elif a == 0:
    print("Nombre a est 0.")
else:
    print("Nombre a est négatif.")