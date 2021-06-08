import  random

# Реализовать алгоритм пузырьковой сортировки.

n = int(input('Enter the quantity of numbers '))
r = 0  # counter of quantity of replacements
n += 1
l = list(range(1, n))  # our list of numbers

random.shuffle(l)

print(list(l))

for rep in range(1, n):
    for i in range(n-1-rep):  # bubble detection cycle and its exclusion
        if l[i] > l[i+1]:
            r += 1
            l[i], l[i+1] = l[i+1], l[i]
            print(l)  # list view after each replacement
print(l)  # our list is sorted
print(r)
