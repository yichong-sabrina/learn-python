# Example 1
L0 = list(range(1,11))
L1 = [x*x for x in range(1,11)]                           # 把要生成的元素放到前面，后面跟for循环，就可以把list创建出来
L2 = [x*x for x in range(1,11) if x%2 == 0]               # for循环后面还可以加上if判断
print('L0 =', L0, '\nL1 =', L1, '\nL2 =', L2)


# Example 2
L3 = [m+n for m in 'ABC' for n in '123']                  # 使用两层循环，可以生成全排列
print('L3 =', L3)


# Example 3
import os
L4 = [d for d in os.listdir()]                            # os.listdir() 列出当前目录下的所有文件名和目录名
print('L4 =', L4)


# Example 4
D = {'Apple':'3', 'Banana':'1', 'Orange':'5'}
L5 = [key + '=' + value for key, value in D.items()]
print('L5 =', L5)


# Example 5
Str = ['HeLlO', 'NiCe', 'BAll', 'biRD']
L6 = [s.lower() for s in Str]                             # 字符串类型的lower()方法：把一个list中所有的字符串变成小写
print('L6 =', L6)


# Practice
L = ['Hello', 'World', 18, 'Apple', None]                 # 非字符串类型没有lower()方法
Lower = [s.lower() for s in L if isinstance(s,str)]
print('L =', L, '\nLower =', Lower)



