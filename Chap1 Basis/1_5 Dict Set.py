# dict
dict_1 = {'Amy':90, 'Bob':80, 'Cindy':70, 'David':60, 'Edgar':50}  # dictionary
# dict内部存放的顺序和key放入的顺序是没有关系的

print('David:', dict_1['David'])
dict_1['Amy'] = 100

print('Bob:', dict_1.get('Bob'))
print('Is Bob in dic_1?','Bob' in dict_1)

print('Alice:', dict_1.get('Alice'))
print('Alice:', dict_1.get('Alice',-99))
print('Is Alice in dic_1?', 'Alice' in dict_1)

dict_1.pop('Edgar')

# set
s1 = set([1,2,3])
s2 = set([2,2,3,3,3,4,4,4,4])
print('s1 = ', s1, '    s2 = ', s2)

s1.add(4)
print('add a key:', s1)
s1.remove(4)
print('remove a key:',s1)

print('s1 & s2:', s1 & s2)
print('s1 | s2:', s1 | s2)
