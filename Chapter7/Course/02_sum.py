def my_sum(num1, num2):
    # print(num1 + num2)
    # return: 返回值
    return num1 + num2

def my_minus(num1, num2):
    # print(num1 - num2)
    return num1 - num2

# print(my_sum(2, 3))
# my_minus(5, 4)
# print(my_minus(5, (my_sum(2, 3))))
num1 = my_sum(2, 3)
print(num1)
num2 = my_minus(5, num1)
print(num2)
