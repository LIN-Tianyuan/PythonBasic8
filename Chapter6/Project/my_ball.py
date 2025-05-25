import random

# 自己的袋子
my_collection = ['rouge', 'rose', 'orange', 'rouge', 'rose', 'jaune', 'rose', 'jaune']
# 商店的袋子
bag_of_balls = ['rose', 'bleu', 'vert', 'orange', 'rouge', 'pourpre', 'vert', 'bleu', 'bleu', 'rouge', 'vert', 'poupre', 'jaune', 'rouge', 'rose', 'rouge', 'vert', 'jaune']
# 抽取出来的球
balls_outputs = []
number = 5
i = 0
while i < number:
    # 实现抽取球的逻辑
    # random.randint(a, b): 从a和b之间任意取一个数，包括a和b
    # selection = random.randint(0, len(bag_of_balls) - 1)
    # print(selection)
    # selection_ball = bag_of_balls[selection]
    # print(selection_ball)
    # random.choice(容器)：随机获取容器里的元素
    selection_ball = random.choice(bag_of_balls)
    # print(selection_ball)
    balls_outputs.append(selection_ball)
    if selection_ball == 'vert':
        my_collection.append(selection_ball)
        print("Excellent!Tu as tiré ta bille verte!")
        break
    else:
        print("Tu as tiré la bille " + selection_ball + ".")
        print("Il restait " + str(number - i - 1) + " tirages.")
    i = i + 1

if not("vert" in my_collection):
    print("Tous les tirages sont faits. Aucune bille verte.")

print("Billes sorties pour ce tirage: ")
print(balls_outputs)
print("La nouvelle collection contient: ")
print(my_collection)