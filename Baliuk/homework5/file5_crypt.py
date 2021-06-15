import string

# Реализуйте шифратор и дешифратор по шифру Цезаря.
# Спросить пользователя, что он хочет сделать - зашифровать или расшифровать файл.
# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла,
# который мы получим на выходе(зашифрованного) и ключ(ключем будет уроваень сдвига).
# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на выходе(расшифрованного) и ключ.

ABC = string.ascii_lowercase
# print(ABC)
l = len(ABC)

crypt_list = []
crypt_str = ''
try:
    user_selection = int(input('If you want to encoding your text - enter \
\"1\",\nif you want to decoding - enter \"2\" '))
    if user_selection == 1:
        encod_name = input('Enter the name of the encoding file ')
        decod_name = input('Enter the name of the decoding file ')

        with open(f'{encod_name}.txt', 'r') as encod:
            my_str = list(encod.read().lower())
        l1 = len(my_str)

        try:
            k = int(input('Enter the key from 1 to 25 - '))
            if k <= 0:
                raise ValueError
            try:
                for i in range(l1):
                    if my_str[i] == ' ':
                        crypt_list.append(' ')
                    else:
                        x = ABC.index(my_str[i])
                        crypt_list.append(ABC[(x + k) % l])
                for j in range(l1):
                    crypt_str += crypt_list[j]
                with open(f'{decod_name}.txt', 'w+') as decod:
                    decod.write(crypt_str)
                print('Your information has been successfully encoded!')
            except ValueError:
                print('Error!!!Enter text only!!!')
        except ValueError:
            print('The key can only be a positive number!')

    elif user_selection == 2:
        decod_name = input('Enter the name of the decoding file ')
        encod_name = input('Enter the name of the encoding file ')

        with open(f'{decod_name}.txt', 'r') as decod:
            my_str = list(decod.read().lower())
        l1 = len(my_str)

        try:
            k = int(input('Enter the key from 1 to 25 - '))
            if k <= 0:
                raise ValueError
            try:
                for i in range(l1):
                    if my_str[i] == ' ':
                        crypt_list.append(' ')
                    else:
                        x = ABC.index(my_str[i])
                        crypt_list.append(ABC[x - k])
                for j in range(l1):
                    crypt_str += crypt_list[j]
                with open(f'{encod_name}.txt', 'w+') as encod:
                    encod.write(crypt_str)
                print('Your information has been successfully decoded!')
            except ValueError:
                print('Error!!!Enter text only!!!')
        except ValueError:
            print('The key can only be a positive number!')
    else:
        print('Incorrect input!')
except ValueError:
    print('Enter a number!')