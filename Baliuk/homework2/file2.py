sample_dict = {
   'class_a': {
      'student1': {
         'name': 'Misha',
         'marks': {
            'math': 90,
            'history': 85
         }
      }
   }
}

# 1. Вывести значение ключа "name";
print(sample_dict['class_a']['student1']['name'])

# 2. Вывести значение ключа "history";
print(sample_dict['class_a']['student1']['marks']['history'])

# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
sample_dict['class_a']['student2'] = {
                                    'name': 'Vasya',
                                    'marks': {
                                        'math': 75,
                                        'history': 95
                                    }
                                }
print(sample_dict)

# 4. Добавить новый класс со студентами (в sample_dict нужно добавить class_b, в котором будет 2 студента);
sample_dict['class_b'] = {
                        'student3': {
                                    'name': 'Sveta',
                                    'marks': {
                                        'math': 80,
                                        'history': 90
                                    }
                                },
                        'student4': {
                                    'name': 'Vika',
                                    'marks': {
                                        'math': 95,
                                        'history': 95
                                    }
                                }
                        }
print(sample_dict)

# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
sample_dict['class_a']['student1']['marks']['physics'] = 90
sample_dict['class_a']['student2']['marks']['physics'] = 80
sample_dict['class_b']['student3']['marks']['physics'] = 85
sample_dict['class_b']['student4']['marks']['physics'] = 90

print(sample_dict)

# 6. Подсчитать средний бал по каждому студенту (результат округлить до 2 знаков после запятой);
sr_bal_stud1 = round((sample_dict['class_a']['student1']['marks']['physics'] + \
                sample_dict['class_a']['student1']['marks']['math'] + \
                sample_dict['class_a']['student1']['marks']['history']) / 3, 2)
sr_bal_stud2 = round((sample_dict['class_a']['student2']['marks']['physics'] + \
                sample_dict['class_a']['student2']['marks']['math'] + \
                sample_dict['class_a']['student2']['marks']['history']) / 3, 2)
sr_bal_stud3 = round((sample_dict['class_b']['student3']['marks']['physics'] + \
                sample_dict['class_b']['student3']['marks']['math'] + \
                sample_dict['class_b']['student3']['marks']['history']) / 3, 2)
sr_bal_stud4 = round((sample_dict['class_b']['student4']['marks']['physics'] + \
                sample_dict['class_b']['student4']['marks']['math'] + \
                sample_dict['class_b']['student4']['marks']['history']) / 3, 2)

print(sr_bal_stud1)
print(sr_bal_stud2)
print(sr_bal_stud3)
print(sr_bal_stud4)

# 7. Создать словарь со средним баллом за каждого студента;
sr_bal_stud_dict = {'Misha': sr_bal_stud1, 'Vasya': sr_bal_stud2, \
            'Sveta': sr_bal_stud3, 'Vika': sr_bal_stud4}

print(sr_bal_stud_dict)

# 8. Определить лучшего студента по успеваемости;
x = max(sr_bal_stud_dict['Misha'], sr_bal_stud_dict['Vasya'], \
        sr_bal_stud_dict['Sveta'], sr_bal_stud_dict['Vika'])  # max point among students
best_stud = list(sr_bal_stud_dict.keys()) \
    [list(sr_bal_stud_dict.values()).index(x)]  # splits dictionary values in a list

print('best student - ' + best_stud)

# 9. Подсчитать средний бал по каждому классу (результат округлить до 2 знаков после запятой);
sr_bal_class_a = round((sr_bal_stud1 + sr_bal_stud2) / 2, 2)
sr_bal_class_b = round((sr_bal_stud3 + sr_bal_stud4) / 2, 2)

print(sr_bal_class_a)
print(sr_bal_class_b)

# 8. Создать словарь со средним баллом за классы;
sr_bal_slas_dict = {'sr_bal_class_a': sr_bal_class_a, \
                    'sr_bal_class_b': sr_bal_class_b}

print(sr_bal_slas_dict)

# 9. Определить лучший класс по успеваемости.
y = max(sr_bal_slas_dict['sr_bal_class_a'], \
        sr_bal_slas_dict['sr_bal_class_b'])  # max point among classes
best_class = list(sr_bal_slas_dict.keys()) \
    [list(sr_bal_slas_dict.values()).index(y)][-1]  # splits dictionary values in a list

print('best class - slass ' + str(best_class))
