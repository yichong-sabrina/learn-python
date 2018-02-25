# Factorial Calculator
def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n


print('fact(5) =', fact(5))
print('fact(10) =', fact(10))


# Tower of Hanoi Puzzle
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1, a, c, b)
    print(a, '-->', c)
    move(n-1, b, a, c)


print('n = 2')
move(2, 'A', 'B', 'C')
print('n = 3')
move(3, 'A', 'B', 'C')
