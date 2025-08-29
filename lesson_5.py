# user_age = int(input('Your age  '))
#
# true = True
# false = False
#
# if user_age:
#     print('*')
#
#
# print(user_age)
#
# user_name = input('Enter name  ').title()
#
# if user_name != 'John' or False:
#     print(f'Hello, {user_name}')
# else:
#     print('go away')

#
# my_string = '5555'
#
# if my_string.isdigit():
#     number = int(my_string)
#     print(number, end=' *** ')
# else:
#     print('not for int')
#     print

side1 = float(input('one'))
side2 = float(input('two'))
side3 = float(input('three'))

s1 = side1 < (side2 + side3)
s2 = side2 < (side1 + side3)
s3 = side3 < (side1+side2)

if s1 and s2 and s3:
    print('triangle')
# elif side2 < (side1 + side3):
#     print('triangle')
# elif side3 < (side1+side2):
#     print('triangle')
else:
    print('no')
