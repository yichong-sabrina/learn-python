from collections import Iterable, Iterator

# 1. Iterable -- 可迭代对象
# 凡是可作用于for循环的对象都是Iterable类型
# List, Str, Dict, Generator都是Iterable类型, Int不是Iterable类型

# 2. Iterator -- 迭代器
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# Generator也是Iterator类型
# 集合数据类型如List, Str, Dict等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象


print('isinstance([], Iterable) =', isinstance([], Iterable))       # List
print('isinstance([], Iterator) =', isinstance([], Iterator))
print('isinstance(iter([]), Iterator) =', isinstance(iter([]), Iterator))


print('isinstance({}, Iterable) =', isinstance({}, Iterable))       # Dict
print('isinstance({}, Iterator) =', isinstance({}, Iterator))
print('isinstance(iter({}), Iterator) =', isinstance(iter({}), Iterator))


g = (x*x for x in range(5))                                         # Generator
print('isinstance(g, Iterable) =', isinstance(g, Iterable))
print('isinstance(g, Iterator) =', isinstance(g, Iterator))


# 3. Python的for循环本质上就是通过不断调用next()函数实现的
# 以下两段代码本质上完全相同
for x in [1, 2, 3, 4, 5]:
    pass


it = iter([1, 2, 3, 4, 5])
while True:
    try:
        # 获得下一个值
        x = next(it)
    except StopIteration:
        # 遇到StopIteration则跳出循环
        break

