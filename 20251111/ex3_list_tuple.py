# Список фраз
texts = [abracadabra]
#text = texts[5] # Будет ошибка
text = texts[0][5]  # преобразование в строку и взятие символа
print(texts, type(texts))
print(text, type(text))
