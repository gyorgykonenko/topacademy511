#Задача: напишите программу, которая позволяет вводить пользователю сумму покупки и возраст.
# Если сумма покупки превышает 100 долларов, предоставляется скидка 10%. Дополнительно, если покупатель старше 65 лет,
# он получает дополнительную скидку 5%.
pokupka_sum_add = input('Введите сумму покупки: ')
add_vozrast = input('Введите ваш возраст: ')
pokupka_sum = float(pokupka_sum_add)
vozrast = int(add_vozrast)
if pokupka_sum <= 0:
    print ('некорректная сумма, повторите попытку')
else:
    if vozrast <=6:
        print ('Возраст не может быть меньше 6 лет!')
    else:
        if pokupka_sum > 100 and vozrast > 65:
            print ('Ваша скидка 15%')
        elif pokupka_sum > 100 and vozrast <= 65:
            print ('Ваша скидка 10%')
        elif pokupka_sum <= 100 and vozrast > 65:
            print ('Ваша скидка 5%')
        else:
            pokupka_sum <= 100 and vozrast <= 65
            print ('У вас нет скидок!')