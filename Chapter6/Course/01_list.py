# 创建列表 list （# option + shift + 5 => 中括号）
leisure = ['swim', 'dance', 'sing']
print(leisure)
# 获取列表长度
print(len(leisure))
# 判断元素是否在列表里
print("basketball" in leisure)
print("dance" in leisure)
# 大小写区分
print("DANCE" in leisure)
# 获取元素下标 index
print(leisure.index('swim'))
# 通过下标index获取列表元素
print(leisure[1])
# 通过下标index修改列表元素 把swim改成了ski
leisure[0] = 'ski'
print(leisure)
# 追加新元素game到列表末尾
leisure.append("game")
print(leisure)
# 插入元素到列表中（不一定在末尾）
leisure.insert(3, "climb")
print(leisure)
print(leisure.index('game'))
# 删除列表中的指定元素
leisure.remove('climb')
print(leisure)
# 删除列表中指定下标的元素
leisure.pop(1)
print(leisure)
# 清空列表
leisure.clear()
print(leisure)

print('----------')
month = ['Janvier', 'Février', 'Mars']
season = ['Automne', 'Hiver', 'Printemps', 'Eté']
# 合并两个列表
various_times = month + season
print(various_times)
print('----------')
# 在原本的列表上添加新的列表元素
month.extend(season)
print(month)
print(season)

print('----------')
rainbow = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
print(len(rainbow))
# 列表切片，用来获取子列表
print(rainbow[1:4])
# 冒号后面的省略不写，就是默认取到列表最后一个元素
print(rainbow[2:])  # print(rainbow[2:7])
# 冒号前面的省略不写，就是默认从第零个元素开始取
print(rainbow[:4])  # print(rainbow[0:4])
# 最后一个元素的下标是-1
print(rainbow[-1])
print(rainbow[-2:])
print(rainbow[-5:-1])

