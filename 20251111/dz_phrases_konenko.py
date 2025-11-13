# Есть изначально пустой список phrases.
# Напишите программу, по которой:
# компьютер сначала запрашивает у пользователя 10 фраз
# и помещает каждую фразу в список phrases;
phrases = [] # пустой список
filtered_phrases = [] # пустой фильтр
kolvo = input('Введите количество фраз: ')
kolvo = int(kolvo)
for i in range(kolvo):
    add_phrases = input("Введите %i-ю фразу: " % (i + 1))
    phrases.append(add_phrases)
# потом компьютер запрашивает у пользователя целое число N;
chislo = input('Введите целое число: ')
chislo = int(chislo)
# далее компьютер выводит построчно фразы из списка phrases,
for add_phrases in phrases:  # перебираем элементы списка
    if len(add_phrases) >= chislo:
        filtered_phrases.append(add_phrases)
        print(add_phrases)
        print(filtered_phrases)
# но только те, чья длина больше, либо равна N.
#    print(phrases.index(add_phrases), " - ", add_phrases)

# for add_color in range(len(raduga)

# Всё то же, что и на 10 баллов, но теперь:
# есть ещё изначально пустой список filtered_phrases (отфильтрованные фразы);
# компьютер копирует из списка phrases в список filtered_phrases такие фразы,
# длины которых больше, либо равны N;
# далее компьютер выводит построчно содержимое списка
# filtered_phrases.
