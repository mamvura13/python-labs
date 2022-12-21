
#1.Потренируйтесь c логическими и побитовыми операторами.
a = True

b = False

print(a and b)

print((a and b) or b)

print((a and b) or not (a and b))

print(a and b or not (a or b) or b)

print(b and b or not a and (a or b or a) or not (a or b))

print(1 << 2)

print(1 & 0 | 1 >> 1)

print(1 & 0 | 1 >> 0)



#2.Напишите программу, которая принимает с клавиатуры 2 числа, сравнивает между собой и выводит на экран наименьшее.
x = int(input("enter a number: "))
y = int(input("enter a number: "))

res = x + y 

print(f"{x} + {y} = {res}")


#3.Напишите программу, которая принимает с клавиатуры 3 числа, сравнивает между собой и выводит на экран наибольшее.
x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))

print(f"the biggest number of the three is { max(max(y,z),x)}")

#4.Напишите программу, которая принимает с клавиатуры 3 числа и выводит на экран количество уникальных чисел.
lst = []
for i in range(3):
    a = int(input("enter a number: "))
    lst.append(a)

print(f"the number of unique numbers is: {len(set(lst))}")

