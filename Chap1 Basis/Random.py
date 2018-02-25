# 引入模块：
# from 模块名 import 方法名

from random import randint   # 引入随机数模块
num = randint(1,100)           # 1-100范围内的整数
bingo = False                 # 设置循环的FLAG

while not bingo:              # 语法：while not
    print("Guess an integer between 1-100!")
    ans = int(input())

    if ans > num:
        print("Too big!")
    if ans < num:
        print("Too small!")
    if ans == num:
        print("Bingo!")
        bingo = True            # 缩进：4个空格

