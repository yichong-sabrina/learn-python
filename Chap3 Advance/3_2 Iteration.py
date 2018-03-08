# 只要是可迭代对象，无论有无下标，都可以迭代
# Example 1 -- Dict
d = {'Alex':90, 'Daisy':60, 'Betty':80}
for k in d:                      # 默认情况下，dict迭代的是key
    print(k)
for v in d.values():             # 迭代value
    print(v)
for k,v in d.items():            # 同时迭代key和value
    print(k,':', v)

# Example 2 -- String
for ch in 'AhiwWjbkr':
    print(ch)


# 可迭代对象 -- collections模块的Iterable类型
from collections import Iterable
print(isinstance(d, Iterable))
print(isinstance('123', Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance(123, Iterable))


# 同时引用两个变量
# Example 3 -- enumerate
for i,value in enumerate(['a', 'b', 'c']):
    print(i, value)

# Example 4
for x,y in [(1,1), (2,4), (3,9)]:
    print(x, y)


# Practice -- 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if not L :
        return (None, None)
    min = L[0]
    max = L[0]
    for v in L:
        if v < min:
            min = v
        if v > max:
            max = v
    return (min, max)


print('findMinAndMax([]) =', findMinAndMax([]))
print('findMinAndMax([7]) =', findMinAndMax([7]))
print('findMinAndMax([7, 2, 5, 9, 4]) =', findMinAndMax([7, 2, 5, 9, 4]))

