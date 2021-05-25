# 1. Открыть тот же файл и перезаписать его содержимое на эту же строку в обратном порядке (задом на перед).

name = input('enter your name')
sername = input('enter your sername')
age = input('enter your age')
with open('new_file.txt', 'w+') as file:
    file.write(f'{name} {sername} - {age}')
    file.seek(0)
    new_data = file.read()
    file.seek(0)
    file.write(new_data.replace(age, '27'))
with open('new_file.txt', 'r+') as file:
    lst = file.read().rstrip('\n')
    print(lst)
    lst1 = lst[::-1]
    print(lst1)
    file.seek(0)
    file.write(lst1)