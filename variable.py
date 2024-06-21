print('I am new to python language')

# print('i am chinasa Ali')
# print('o----')
# print(' ||||')
# print('*' * 10)

# VARRIABLES

price = 10
rating = 4.9
name = 'chinasa'
is_published = True
print(price,rating,name,is_published)

name ='john smith'
age = 20
is_new = True
print(f"My name is {name} and I am {age} years old and it is {is_new} that I am new.")

# INPUTING THINGS ON SCREEN

fullname = input('What is your name? ')
print('Hi ' + fullname)

surname = input('what is your surname? ')
color = input('what is your favourite color? ')
# print('chinasa likes ' + color)
print(surname + ' likes ' + color)

# TYPE CONVERSION?

birth_year = input('birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

weight = input('whats your weight: ')
kilogram =int(weight) * 0.45
print(kilogram)

# STRINGS

email = ''' 
Hi john,

here is the support email to you.
Thank you!
'''

print(email)

course = 'python for beginners'
another = course [:]
# print(course[0])
# print(course[-1])
# print(course[0:3])
print(another)

full_name = 'jennifer'
print(full_name[1:-1])