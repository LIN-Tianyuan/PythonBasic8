name = "Ming"
age = 19
money = 50.0
print("Mon nom est " + name + ".")
print("Mon âge est " + str(age) + ".")
# %s 先预定一个位置，在最后再补上，%s代表string
print("Mon nom est %s." %name)
# %d decimal
print("Mon âge est %d." %age)
# %f float
print("Mon argent est %f." %money)
print("Mon nom est %s. Mon âge est %d. Mon argent est %f." %(name, age, money))