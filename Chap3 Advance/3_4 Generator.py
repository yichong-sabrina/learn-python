# Example 1
g = (x*x for x in list(range(1,4)))
print('g = x*x for x in [1,2,3]')
for n in g:
    print('g:', n)


# Example 2
def fib_1(max):              # fib_1() is an ordinary function
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'Done'
fib_1(5)


def fib_2(max):               # fib_2() is a generator function
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'Done'


f = fib_2(8)                  # f is a generator
print('f = fib_2(8)')
for n in f:
    print('f:', n)


# Example 3
def odd():
    print('Step 1')
    yield 1
    print('Step 2')
    yield 3
    print('Step 3')
    yield 5


o = odd()                     # ??? 显示不了yield的值???
next(o)                       # 每次调用next()的时候执行，遇到yield语句返回
next(o)                       # 再次执行时从上次返回的yield语句处继续执行
next(o)


# Example 4
h = fib_2(5)
print('h = fib_2(5)')
while True:
    try:
        x = next(h)
        print('h:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# Practice -- 杨辉三角
def triangles():
    a = [1]
    l = 1
    while True:
        yield a
        b = [a[n] + a[n+1] for n in list(range(l-1))]
        a = [1] + b + [1]
        l = len(a)


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

