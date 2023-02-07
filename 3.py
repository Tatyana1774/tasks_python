#Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator #Импортируем нужный модуль и объявляем словарь
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
print(d)

# 2 вариант

result = dict(sorted(d.items(), key=operator.itemgetter(1))) #Сортируем в порядке возрастания
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)
