import string

name = input('enter your name')
age = input('enter your age')
sex = input('enter your gender')

about_me_concat = 'Hello! My name is '+ name +'. I\'m '+ age +' and I\'m a '\
 + sex + '.'
print(about_me_concat)
about_me_percent = 'Hello! My name is %s. I\'m %s and I\'m a %s.' % (name, age, sex)
print(about_me_percent)
about_me_format = 'Hello! My name is {}. I\'m {} and I\'m a {}.'.format(name, age, sex)
print(about_me_format)
about_me_fstring = f'Hello! My name is {name}. I\'m {age} and I\'m a {sex}.'
print(about_me_fstring)

str0 = about_me_fstring.split('.')
str1 = str0[0]
str2 = str0[1]
print(str0)
print(str1)
print(str2)


about_my_friend = about_me_fstring.replace('My','My friend\'s').replace('I\'m', \
'She\'s', 2).replace(name, 'Nata').replace(str(age), '26').replace(sex, 'female')

print(about_my_friend)

print(type(about_me_fstring))

list_from_str = about_me_fstring.split()
print(list_from_str)

print(type(list_from_str))

str_from_list = ' '.join(list_from_str)
print(str_from_list)
print(type(str_from_list))

print(about_me_fstring.swapcase())
