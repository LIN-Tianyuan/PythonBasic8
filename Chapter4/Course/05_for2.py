# 打印0-10，如果range里只有一个参数，就是0到它前面的那个数
for element in range(11):
    print(element)

print('----------')

# 打印1-10，如果range里有两个参数，就是前面那个参数到后面那个参数（的前面那个数）
for element in range(1, 11):
    print(element)

print('----------')

# 打印1,3,5,7,9，range里有三个参数，第三个参数表示步伐
for element in range(1, 11, 2):
    print(element)

