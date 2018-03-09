# 1. Map
# map()接收两个参数, 一个是函数, 一个是Iterable
# map()将传入的函数依次作用到序列的每个元素, 并把结果作为新的Iterator返回
# map()返回的是一个Iterator, 也就是一个惰性序列, 所以要强迫map()完成计算结果, 需要用list()获得所有结果并返回list


x_1 = list(range(1,6))
y_1 = list(map(lambda x: x * x, x_1))
print('x_1 =', x_1, '\ny_1 =', y_1)


# 2. Reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 注意f必须接收两个参数


from functools import reduce
def prod(L):
    return reduce(lambda x,y: x*y, L)
print('prod([1, 3, 5, 7, 9] =', prod([1, 3, 5, 7, 9]))


# Practice 1 -- str2int, str2float
def char2num(ch):
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dict[ch]


def str2int(str):
    return reduce(lambda x,y: 10*x+y, list(map(char2num, str)))


def str2float(str):
    s = str.split('.')
    int_part = reduce(lambda x,y: 10*x+y, list(map(char2num, s[0])))
    dec_part = reduce(lambda x,y: 10*x+y, list(map(char2num, s[1]))) * 10 ** (-len(s[1]))
    return int_part + dec_part


print('str2int(\'123456\') =', str2int('123456'))
print('str2float(\'123.456\') =', str2float('123.456'))


# Practice 2 -- Normalized name
def normalize(str):
    s1 = str[0]
    s2 = str[1:]
    return s1.upper() + s2.lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print('L1 =', L1, '\nL2 =', L2)


