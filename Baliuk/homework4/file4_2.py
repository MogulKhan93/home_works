# Написать программу которая просит у пользователя ввести его любимое число.
# Если ввод число, тогда поблагодорить пользователя за сотрудничество и завершить программу.
# Если ввод не число, тогда попросить его быть более внимательным и ввести именно число.
# Если неправильный ввод более 3 раз, перейти на более грубое предупреждение.
# Если неправильный ввод более 5 раз, дать пользователю последний шанс.
# Если ввод по прежнему не число, тогда обругать пользователя и завершить программу.


def inp():
    x = input('Enter your favorite number ')
    return x
def f1():
    print('Please, be more careful and enter the number itself, >= 0')
def f2():
    print('Be more careful!The number must be >= 0')
def f3():
    print('Enter a number >=0! I give one last chance!')
def f4():
    print('Fu**ng user..Goodbye!')


att = 0  # quantity of attempts

for i in range(7):
    a = inp()
    try:
        if int(a) < 0:
            att = i + 1
            if 3 < att <= 5:
                f2()
                continue
            elif att == 6:
                f3()
                continue
            elif att > 6:
                f4()
                break
            else:
                f1()
                continue
        else:
            print(f'Your favorite number is {int(a)}. Good job!')
            break
    except ValueError:
        att = i + 1
        if 3 < att <= 5:
            f2()
            continue
        elif att == 6:
            f3()
            continue
        elif att > 6:
            f4()
            break
        else:
            f1()
            continue
