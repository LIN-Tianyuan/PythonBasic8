# 定义函数
# def 函数名(传入参数):
#     函数体

"""
def greet():
    print("Salut, Alex")
"""
# name: 形式参数
"""
def greet(name):
    print("Salut, " + name + "!")
"""

def greet(firstname, lastname):
    print("Salut, " + firstname + lastname + "!")


# 调用函数
# "Alex": 实际参数
"""
greet("Alex")
greet("Luna")
greet("Thibaut")
"""
# greet("LIN", "Tianyuan")

# 默认参数
def season_pref(season="Eté"):
    print("Ma saison préféré est: " + season + ".")

# season_pref("Printemps")
season_pref()
season_pref("Printemps")
