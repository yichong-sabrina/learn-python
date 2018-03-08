# Example 1
L1 = ['Alice', 'Bob', 'Cindy', 'David', 'Ella', 'Frida']
print('L1[1:3] =', L1[1:3])
print('L1[-3:-1] =', L1[-3:-1])
print('L1[:] =', L1[:])


# Example 2
L2 = list(range(100))
print('L2[:10] =', L2[:10])           # First ten numbers
print('L2[-10:] =', L2[-10:])         # Last ten numbers
print('L2[:10:2] =', L2[:10:2])       # First ten numbers, take one for every two
print('L2[::5] =', L2[::5])           # All numbers, take one for every five


# Example 3 -- Tuple
T = (0, 1, 2, 3, 4, 5)
print('T[:3] =', T[:3])               # Still a tuple


# Example 4 -- String
S = 'ABCDEFG'
print('S[:5] =', S[:5])               # A string can be viewed as a list


# Practice -- TRIM
def trim(s):
    if s == '':                       # When s = '', both s[0] and s[-1] are nonsense!
        return s
    if s[0] == ' ':
        s = s[1:]
        return trim(s)
    elif s[-1] == ' ':
        s = s[:-1]
        return trim(s)
    else:
        return s


print('trim(\'   hello!  \') =', trim('   hello!  '))
print('trim(\'    \') =', trim('    '))
print('trim(\'\') =', trim(''))


