# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in a:
    if elem < 5:
        print(elem)

# 2 вариант
print(list(filter(lambda elem: elem < 5, a)))

# 3 вариант

print([elem for elem in a if elem < 5])