num = [36, 5, -12, 9, -21]
print(sorted(num))
print(sorted(num, key=abs))
print(sorted(num, key=abs, reverse=True))


s = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(s))
print(sorted(s, key=str.lower))



# 用一组tuple表示学生名字和成绩, 用sorted()对其分别按名字和成绩排序
def by_name(t):
    return t[0]
def by_grade(t):
    return t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L_1 = sorted(L, key=by_name)
L_2 = sorted(L, key=by_grade, reverse=True)
print('by_name:', L_1, '\nby_grade_high2low:', L_2)

