# ----- Default Arguments -----
def power(x, n=2):
    ans = x
    while n > 1:
        ans = ans * x
        n = n - 1
    return ans


print('power(3, 4) =', power(3, 4))
print('power(6) =', power(6))


# Precautions:
# 1.Default parameters must point to immutable objects
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


# Modify the code
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


# ----- Variable Arguments -----
def mycalc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i ** 2
    return sum


num = [2, 5, 8]
print('mycalc(1,2,3,4) =', mycalc(1,2,3,4))
print('mycalc(*num) =', mycalc(*num))


# ----- Keyword Arguments -----
def person(name, age, **kw):
    print('Name:', name, 'Age:', age, 'Other:', kw)


extra = {'City':'HK', 'Gender':'M'}
person('Bob', 30)
person('Bob', 30, City = 'HK', Gender = 'M')
person('Bob', 30, **extra)


# ----- Keyword-Only Arguments -----
def person_2(name, age, *, city, gender):
    print('Name:', name, 'Age', age, 'City:', city, 'Gender:', gender)


extra_2 = {'city':'HK', 'gender':'M'}
person_2('Bob', 30, city = 'HK', gender = 'M')
person_2('Bob', 30, **extra_2)
# person_2('Bob', 30)    ERROR: no keyword-only arguments
# person_2('Bob', 30, 'HK', 'M')    ERROR: four positional arguments


