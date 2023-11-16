# TODO Найдите количество книг, которое можно разместить на дискете
DATA_VOLUME = 1.44  # Информационный объём дискеты
kByte_in_mByte = 1024  # Перевод Мб в Кб
Byte_in_kByte = 1024  # Перевод Кб в байты

pages = 100  # Количество страниц в книге
strings = 50  # Количество строк на странице
symbols = 25  # Количество символов в строке
bytes_in_one_symbol = 4  # Количество байтов на один символ

bytes_in_one_book = pages * strings * symbols * bytes_in_one_symbol  # Количество байтов в одной книге
data_volume_in_bytes = DATA_VOLUME * kByte_in_mByte * Byte_in_kByte  # Количество байтов на дискете

amount_of_books = data_volume_in_bytes // bytes_in_one_book
print("Количество книг, помещающихся на дискету:", int(amount_of_books))
