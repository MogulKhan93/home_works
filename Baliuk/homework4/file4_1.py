import  random

# Реализовать алгоритм пузырьковой сортировки.

def x(lis, r):
    for rep in range(1, n):
        for i in range(n-1-rep):  # bubble detection cycle and its exclusion
            if lis[i] > lis[i+1]:
                r += 1
                lis[i], lis[i+1] = lis[i+1], lis[i]
                # print(lis)  # list view after each replacement
    print(lis)  # our list is sorted
    print(r)
    return lis, r

n = int(input('Enter the quantity of numbers '))
r = 0  # counter of quantity of replacements
n += 1
lis = list(range(1, n))  # our list of numbers

random.shuffle(lis)

print(list(lis))

x(lis, r)
