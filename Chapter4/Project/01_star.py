"""
*********
*********
*********
*********
*********
*********
*********
*********
*********
"""

"""
*
*
*
*
*
*
*
*
*
"""
"""
for i in range(1, 10):
    print("*********")
"""

"""
# 打印一行9颗星星
for i in range(9):
    # print是默认自动换行的，如果要想不换行，我们需要在末尾加上end=""
    print('*', end="")

print()
print('-----------')

# 打印一列9颗星星
for i in range(9):
    print('*')
"""
"""
for i in range(1, 10):
    print("*", end="")
    print(9 * '*')

# *********
for i in range(1, 10):
    for i in range(1, 10):
        print('*')
    print('*')
"""

# 嵌套循环
# 外层循环i 控制行
for i in range(1, 10):
    # 内层循环j 控制列
    for j in range(i):
        # print是默认自动换行的，如果要想不换行，我们需要在末尾加上end=""
        print('*', end="")
    # 如果只是print()，代表换行
    print()
