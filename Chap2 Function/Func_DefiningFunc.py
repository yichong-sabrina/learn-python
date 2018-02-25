# Fun: Calculate the absolute value
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Invalid Operand Type: Operand Must Be int_or_float.')
    if x >= 0:
        return x
    else:
        return -x
# Test
print('my_abs(-58) =', my_abs(-58))
# print('my_abs(\'-123\') =', my_abs('-123'))


# Fun: Solve a Quadratic Eequation
import math
def quadratic(a,b,c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('The equation has no real roots!')
    elif delta == 0:
        root = -2 * a / b
        return root
    else:
        root_1 = (-b + math.sqrt(delta)) / (2 * a)
        root_2 = (-b - math.sqrt(delta)) / (2 * a)
        return root_1, root_2

# Test
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('Test Failed!')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('Test Failed!')
else:
    print('Test Success!')