# напишите программу, которая запрашивает у пользователя числа до тех пор, пока не будет введено число 0.
# После завершения ввода, программа должна вывести сумму всех введённых положительных чисел.
# ввод переменной на количество ввода
kolvo_enters = 0
# ввод переменной для памяти предыдущего числа
chislos = 0
while True:
    chislo = input('Введите число: ')
    chislo = int(chislo)
    # подсчет суммы положительных чисел
    if chislo > 0:
        chislos = chislo + chislos
        kolvo_enters = kolvo_enters + 1
    elif chislo < 0:
        kolvo_enters = kolvo_enters + 1
    else:
        print ('Вы ввели Ноль. Конец. У вас было', kolvo_enters, 'попыток(и)', 'Сумма введенных чисел: ', chislos)
        chislos = 0; kolvo_enters = 0