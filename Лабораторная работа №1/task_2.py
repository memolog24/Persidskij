list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

amount_of_players = len(list_players)  # Общее количество игроков
half = int(amount_of_players / 2)  # Половина от общего количества игроков
team_1 = list_players[::2]  # Команда 1
team_2 = list_players[1::2]  # Команда 2

print(team_1)
print(team_2)
# TODO Разделите участников на две команды
