# List
MyClass = ['Alice', 'Bob', 'Cindy',
           'David', 'Edgar', 'Frida']
print(MyClass[0])                                      # Subscript begins from 0
print(MyClass[-1])                                     # Subscript -1 represents the last element
length = len(MyClass); print(length)                   # len( )

MyClass.append('George')                              # Add elements: append / insert
MyClass.insert(0, 'Zero')
print(MyClass)

MyClass.pop()                                          # Delete elements: pop
MyClass.pop(-3)
print(MyClass)

MyClass[1] = 'Anna'                                   # Replace elements
print(MyClass)

NextClass = ['ABC', 1, 2.345, True, MyClass]          # Different types of elements can be included in one list
print(NextClass)
print(NextClass[-1][1])

Empty = [ ]                                             # Empty List
print(Empty, len(Empty))


# Tuple
Tuple_1 = (1, 2, 3)                                     # Elements in tuples cannot be changed
Tuple_2 = (1, )                                         # A tuple with one element must include a comma!!
Typle_3 = ( )                                           # Empty tuple
print(Tuple_1, Tuple_2, Typle_3)
