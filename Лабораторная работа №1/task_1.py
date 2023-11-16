numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
propusk = 4 # Индекс элемента None в списке
summa = sum(numbers[:propusk] + numbers[propusk+1:])
dlina = len(numbers)
srednee = summa / dlina
numbers[4] = srednee # Присваиваем пропущенному элементу значение среднего арифметического
print("Измененный список:", numbers)
