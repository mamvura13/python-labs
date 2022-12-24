
#1.Напишите функцию, которая принимает массив из 10 чисел и возвращает их сумму.

def find_sum(s):
    return sum(s)

s = list()
for i in range(10):
    s.append(int(input()))

print(find_sum(s))



#Задание 2
#Напишите функцию, которая принимает массив чисел и возвращает количество чисел равных нулю.


def counting_zero(n):
    x = 0
    for i in range(len(n)):
        if n[i] == 0:
            x += 1
            return x

n = list()
for i in range(10):
    n.append(int(input()))

print(counting_zero(n))


#Задание 3
#Напишите программу, в которой задается натуральное число n и выводится лестница из n ступенек, i-я ступенька должна состоять из чисел от 1 до i без пробелов.


def steps(n):
    for i in range(1, n + 1):
        l = ''
        for j in range(1, i + 1):
            l = l + str(j)
        print(l)
    return 'End'

n = 0
n = int(input())

print(steps(n))


#Задание 4
#Напишите программу, в которой задается натуральное число n и выводится пирамида из n ступенек, i-я ступень должна состоять из чисел от 1 до i и обратно без пробелов.


def steps(n):
    for i in range(1, n + 1):
        l = ''
        for j in range(1, i + 1):
            l = l + str(j)
        for j in range(i - 1, 0, -1):
            l = l + str(j)
        print(l)
    return 'End'

n = 0
n = int(input())

print(steps(n))