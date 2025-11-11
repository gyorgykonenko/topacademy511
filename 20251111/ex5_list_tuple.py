# Список чисел
pet_names = [] # пустой список

for i in range(3):
    name = input("Введите имя питомца, вариант %i: " % (i + 1))
    pet_names.append(name)

print("Ваш список:", pet_names)
print("Еще раз ваш список")

for name in pet_names: # перебираем элементы списка
    print(name, end ", ")
    
