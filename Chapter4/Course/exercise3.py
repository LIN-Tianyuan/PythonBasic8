# 定义自增变量i
i = 0
# 定义变量存储和
sum_number = 0
while i < 101:
    # 判断i是否为偶数
    if i % 2 == 0:
        # 如果是偶数再加
        sum_number = i + sum_number
    # 每次最后一定要自增i，避免死循环
    i = i + 1
print(sum_number)