# If, Else, Elif
age = 12
if age >= 18:
    print('Your age is',age)
    print('You are an adult')
elif age >= 6:
    print('Your age is',age)
    print('You are a teenager')
else:
    print('Your age is',age)
    print('You are a kid')

x = 1                                     # Any non-zero constant value equals True
if x:
    print('You are beautiful')

# Input
year = int(input('Year of Birth:'))
if year <= 2000:
    print('Your age is',2018-year)
    print('You are an adult')
elif year <= 2012:
    print('Your age is',2018-year)
    print('You are a teenager')
else:
    print('Your age is',2018-year)
    print('You are a kid')