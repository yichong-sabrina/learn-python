# filter()与map()工作方式类似, 不同之处在于:
# filter()把传入的函数作用于每个元素, 根据返回值是True还是False决定保留还是丢弃该元素


# Example 1 -- 删除偶数
def is_odd(x):
    return x % 2 == 1


a = [1, 2, 4, 7, 9, 10]
print(list(filter(is_odd, a)))


# Example 2 -- 删除空字符串
def not_empty(s):
    return s and s.strip()


b = ['A', None, 'B', '', '\t', 'C', '   ']
print(list(filter(not_empty, b)))


# Example 3 -- 求素数
def odd_seq():      # 生成从3开始的奇数序列
    n = 3
    while True:
        yield n
        n = n + 2


def not_divisible(n):
    return lambda x: x % n > 0


def prime_seq():
    yield 2
    it = odd_seq()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)   # 删去序列中所有可被n整除的数


for i in prime_seq():
    if i < 10:      # 打印10以内的素数
        print(i)
    else:
        break


# Practice -- 求回数
def is_palindrome(num):
    s = str(num)
    return s[::-1] == s[:]      # s[::-1]即可反转字符串


def palindrome(n):
    print(n, '以内的所有回数如下：')
    return list(filter(is_palindrome, range(1,n)))


print(palindrome(200))




