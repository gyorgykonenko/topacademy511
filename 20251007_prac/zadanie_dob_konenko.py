tekgod = input('Введите текущий год? ')
tekmes = input('Введите текущий месяц? ')
rojd_god = input('Ваш год рождения? ')
rojd_mes = input('и месяц рождения: ')
rojdeniya = int(tekgod) - int(rojd_god)
if tekmes >= rojd_mes:
    dob_number = int(rojdeniya)
else:
    dob_number = int(rojdeniya) - 1
if dob_number <= 0:
    print ('год введен неверно, попробуйте снова')
# от 0 до 6 дошкольник
elif dob_number <= 6:
    print ('Вы дошкольник, вам ' + str (dob_number))
elif dob_number <= 17:
# от 7 до 17 школьник
    print ('Вы школьник, вам ' + str (dob_number))
# от 18 до 24 студент
elif dob_number <= 24:
    print ('Вы студент, вам ' + str (dob_number))
# от 25 до 150 взрослый
elif dob_number < 150:
    print ('Вы взрослый, вам ' + str (dob_number))
# от 150 долгожитель
else:
    print ('Вы долгожитель, вам ' + str (dob_number))