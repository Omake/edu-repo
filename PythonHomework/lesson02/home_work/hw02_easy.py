# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


fruits = ["Апельсин", "Мандарин", "Нектарин", "Томат"]
i = 0


while len(fruits) > i:
    print("{}.{:>12}".format(i+1, fruits[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


firstList = [1, 2 ,3, 4, 5,"собака", "кошка", "ягуар"]
secondList = [5, 6, 2, 3, 3.4, "кошка"]


for currentElement in firstList:
    if currentElement in secondList:
        firstList.pop(currentElement)
print("Первый список: ", firstList)
print("Второй список: ", secondList)
print("Первый список с удалением из него элементов второго списка: ",firstList)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


numbersList = [345, 213, 123, 690, 6843, 4542, 878, 54545, 623, 1231234]
newList = []


for element in numbersList:
    if element % 2 == 0:
        newList.append(element/4)
    else:
        newList.append(element * 2)
print("После изменения согласно условиям задания, новый список выглядит следующим образом: ", newList)