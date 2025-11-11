# Список чисел
raduga = [] # пустой список

for i in range(7):
    add_color = input("Введите цвет радуги, вариант %i: " % (i + 1))
    raduga.append(add_color)

print("Ваш список:", raduga)
print("Еще раз ваш список")

for add_color in raduga: # перебираем элементы списка
    print(add_color)
    
