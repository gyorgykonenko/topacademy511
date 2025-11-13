#Задача 1 [8 баллов]
# Задвоить элементы в списке. То есть компьютер превращает список[4, print, "xyz", None]
# в список[4, 4, print, print, "xyz", "xyz", None, None]
my_spisok = [4, print, "xyz", None]
my_spisok2 = my_spisok * 2
print (my_spisok)
print (my_spisok2)
#
#Задача 2 [10 баллов]
chislos = []  # пустой список
# Компьютер спрашивает у пользователя, сколько тот хочет положить в список целых чисел.
kolvo_chislos = input('Введите количество чисел для списка: ')
kolvo_chislos = int(kolvo_chislos)
# Далее указанное число раз компьютер запрашивает у пользователя эти числа.
for i in range(kolvo_chislos):
    add_chislos = input("Введите %i-е число: " % (i + 1))
    chislos.append(add_chislos)
for add_chislos in chislos:  # перебираем элементы списка
    # Потом компьютер выводит построчно элементы списка, указывая их индекс.
    print(chislos.index(add_chislos), " - ", add_chislos)
# Затем удаляет из списка те числа, что находятся в нём под нечётными индексами(счёт с нуля).
# Потом компьютер опять выводит построчно элементы списка, указывая их индекс.
