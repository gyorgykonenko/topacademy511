#result = 0
#znam = int(input('Введите число, я найду обратное:'))
#try:
#    result = 1 / znam
#except ZeroDivisionError:
#    result = None
#if result:
#    print('Обратное равно ', result)
#
# Написать программу, которая спрашивает возраст, выбрасывает исключение,
# если введенное число отрицательное, в противном случае считает год рождения.
dob_itog = 0
dob = input('Введите свой возраст: ')
try: # Проверим на значение строка или пустота
    dob = int(dob)
except ValueError:
    print('Ответ должен быть числом')
else:
    try:
        if dob < 0:
            print ('Отрицательный возвраст!')
        else:
            dob_itog = 2025 - dob
            print('Ваш год рождения - ', dob_itog)
    except dob:
        print('Ошибка')