tekgod = input('Введите текущий год? ')
rojdenie = input('Сколько Вам лет? ')
rojdeniya = int(tekgod) - int(rojdenie)
dob_number = int(rojdeniya)
if dob_number <= 0:
    print ('число введено неверно, попробуйте снова')
else:
    print ('Ваш год рождения - ' + str (dob_number))