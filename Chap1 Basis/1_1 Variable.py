# 整型 浮点型
print(4/7)                                        # 整型运算输出结果总是精确的: 浮点型
print(1.23e3, 12.3e2)

# 字符串
print('I\'m \"Sabrina\"\nWho are you?')      # 转义字符\',\",\n,\t,\\
print('\\\t\\')
print(r'\\\t\\')                                 # r'...'表示'...'内禁止转义
print(r'Hello,"Sabrina"!')
print('''Line 1
Line 2
Line 3''')                                       # '''...'''换行
print(r'''Hi,\n
I am Sabrina''')                                # r'''...'''禁止转义

# 布尔型(bool)
print(True and False)                            # 二值: True, Falese; 运算: and, or, not
print(1>3 or 1<=3)
print(not 1==2)

# 空值: None

# 常量: 英文大写
# print(PI)
import math
print(math.pi)

# 动态语言
a = 123; print(a)
a = 'ABC'; print(a)                               # 同一个变量可以反复赋值，而且可以是不同的类型
# 静态语言 int a = 3

print(20 / 3)
print(20 // 3)                                     # 地板除
print(20 % 3)                                      # 取余
