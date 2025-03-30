"""
i = 0
while i <= 10:
    print(i)
    if i == 8:
        # break表示退出循环，后面的循环就不再走了
        break
    i = i + 2
"""

i = 0
while i <= 10:
    # 判断是否是偶数，是就打印
    if i % 2 == 0:
        print(i)
        # 如果是8就跳出循环
        if i == 8:
            break
    # 自增
    i = i + 1

