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

"""
# season_pref("Printemps")
season_pref()
season_pref("Printemps")
"""

# 参数列表：*参数
# 可以在调用的时候不限制传参
def visit(*countries):
    for country in countries:
        print("J'ai visité ce pays: " + country + ".")

"""
# visit("France", "China")
visit("Germany", "France", "China")
"""

def list_game(competitor_1, competitor_2, competitor_3):
    print("Concurrents du jour: " + competitor_1 + " " + competitor_2 + " " + competitor_3 + ".")

"""
list_game("Alex", "Lucas", "Laurent")
# 位置参数
list_game("Lucas", "Laurent", "Alex")
# 关键字参数
list_game(competitor_3="Alex", competitor_2="Laurent", competitor_1="Lucas")
"""


