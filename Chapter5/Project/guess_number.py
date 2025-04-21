import random

# 什么条件是一定正确的？ True
# 用随机数定义电脑的值
computer = random.randint(1, 100)
print(computer)
count = 0
# 用户猜数
# 常用的套路：
# 如果你不知道条件是什么，或者说你想它先无论如何能进入循环，你就把条件设置为True
# 那如何退出循环呢？就在条件成立时用break
while True:
    player = int(input("请输入一个数字："))
    count = count + 1
    if player > computer:
        print("您猜大了，请往小了猜！")
    elif player < computer:
        print("您猜小了，请往大了猜！")
    else:
        print("您猜对了！您一共猜了 " + str(count) + " 次！")
        break