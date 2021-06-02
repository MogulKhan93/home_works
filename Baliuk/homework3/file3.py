# 1. Создать эмуляцию системы входа и регистрации для пользователей.
# 2. При запуске программы, пользователя должно спросить проходил ли он
# регистрацию на нашем ресурсе, если да, тогда предложить ему ввести логин и
# пароль от его учетной записи.
# 3. Если данные верны вывести сообщение об успешном входе в систему, если
# нет - тогда сообщить об это.
# 4. Если пользователь не регистрировался на ресурсе, тогда спросить не желает
# ли он пройти регистрацию.
# 5. Если желает, взять от него необходимые данные и вывести об успешной
# регистрации, если не желает регистрироватся - пожелать удачи.
# 6. Данные о зарегестрированных пользователях хранить в файле 'users.txt',
# по желанию можете создать файл для логирования событий регистрации и входа.

regist_quest = input('Hello. Have you previously registered on our resource? \
                      \nif \"yes\" - enter \"1\" \nif \"no\" - enter \"2\" ')

with open('users.txt', 'r') as file:
    users_data = file.readlines()

l = len(users_data)  # quantity of registered users
users_data_dict = {}

for i in range(l):
    users_data_dict.update({users_data[i].split()[0]: users_data[i].split()[1]})  # creating a dictionary with users data

if regist_quest == '1':
    user_login = input('Enter your login and password! \nlogin - ')
    user_pass = input('password - ')

    for log in users_data_dict:
        if user_login == log:  # checking the compliance of the user-entered login to the database
            if user_pass == users_data_dict.get(log):  # checking the compliance of the user-entered password to the database
                print('Successful login!')
                break
            else:
                print('Invalid login or password!')
                break

    else:
        print('Invalid login or password!')

elif regist_quest == '2':
    desire_reg = input('You want to register? \nif \"yes\" - enter \"1\" \
                        \nif \"no\" - enter \"2\" ')
    if desire_reg == '1':
        new_user_login = input('Login cannot be empty! Enter your login ')
        new_user_pass = input('Password cannot be empty! Enter your password ')

        for log in users_data_dict:
            if new_user_login == '' or new_user_pass == '':
                print('Incorrect input!')
                break
            elif new_user_login == log:
                print('That username is taken. Try another!')
                break

        else:
            with open('users.txt', 'r') as new_data:
                new_users_data = new_data.readlines()
            print(new_users_data)
            with open('users.txt', 'a') as new_data:
                new_data.write(f'\n{new_user_login} {new_user_pass}')
            with open('users.txt', 'r') as new_data:
                new_users_data = new_data.readlines()
            print(new_users_data)

            print('Registration was successful!')

    elif desire_reg == '2':
        print('Okay. Good Luck!')
    else:
        print('Incorrect input!')
else:
    print('Incorrect input!')