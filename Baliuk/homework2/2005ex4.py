# 1. Считать данные с файла и сохранить только уникальные значения;

with open('info_ex4.txt', 'r', encoding='UTF-8') as file:
    lst = file.readlines()
print(lst)
print(type(lst))
l = len(lst)
lst[l-1] = lst[l-1] + '\n'
set_from_list = set(lst)
print(set_from_list)
print(type(set_from_list))

# 2. Записать их в новый файл в алфавитном порядке (каждый элемент в новой строке).

list_from_set = list(set_from_list)
print(list_from_set)
print(type(list_from_set))
sorted_list = sorted(list_from_set)
print(sorted_list)
print(type(sorted_list))
with open('new_info_ex4.txt', 'w+', encoding='UTF-8') as file:
    file.seek(0)
    file.writelines(sorted_list)