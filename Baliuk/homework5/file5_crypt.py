import string

# Реализуйте шифратор и дешифратор по шифру Цезаря.
# Спросить пользователя, что он хочет сделать - зашифровать или расшифровать файл.
# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла,
# который мы получим на выходе(зашифрованного) и ключ(ключем будет уроваень сдвига).
# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на
# выходе(расшифрованного) и ключ.

ABC = string.ascii_lowercase
print(ABC)
l = len(ABC)
crypt_list = []

def encod_func(z1, z2):
    return (z1 + z2) % l

def decod_func(z4, z5):
    return z4 - z5

def crypt_func(z, file_name1, file_name2):
    with open(f'{file_name1}.txt', 'r') as file:
        my_str = list(file.read().lower())
    l1 = len(my_str)
    try:
        crypt_str = ''
        k = int(input('Enter the key from 1 to 25 - '))
        if k <= 0 or k > 25:
            raise ValueError
        try:
            for i in range(l1):
                if my_str[i] == ' ':
                    crypt_list.append(' ')
                else:
                    x = ABC.index(my_str[i])
                    crypt_list.append(ABC[z(x, k)])
            for j in range(l1):
                crypt_str += crypt_list[j]  # list --> str
            with open(f'{file_name2}.txt', 'w+') as file1:
                file1.write(crypt_str)
            print('Congratulations! Your information has been successfully \
encoded(decoded)!')
        except ValueError:
            print('Error!!!Only text can be encoded or decoded!!!')
    except ValueError:
        print('The key can only be a positive number from 1 to 25!')

def general_func(user_selection):
    if user_selection == 1:
        file_name1 = input('Enter the name of the encoding file ')
        file_name2 = input('Enter the name of the decoding file ')
        crypt_func(encod_func, file_name1, file_name2)
    elif user_selection == 2:
        file_name1 = input('Enter the name of the decoding file ')
        file_name2 = input('Enter the name of the encoding file ')
        crypt_func(decod_func, file_name1, file_name2)
    else:
        print('Incorrect input!')
try:
    user_selection = int(input('If you want to encoding your text - enter \
\"1\",\nif you want to decoding - enter \"2\" '))

    general_func(user_selection)
except ValueError:
    print('Enter a number!')