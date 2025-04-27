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