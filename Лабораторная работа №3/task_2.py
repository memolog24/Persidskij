# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, delimiter=","):
    first = first.split(delimiter)
    second = second.split(delimiter)

    intersection = sorted(set(first).intersection(second))
    return intersection

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

final_list = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(final_list)
# TODO Провеьте работу функции с разделителем отличным от запятой
