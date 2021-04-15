# тут пока тестирую код из модуля gamecity
from collections import defaultdict

cities = defaultdict(list)
city_key_bot = ''
city_key_client = ''
city = 'Анапа'

with open('CITIES.md', 'r', encoding='Windows-1251') as file:
    for line in file:
        cities[line[0].lower()].append(line[:-1])
print(cities)


def game_city(client_message_city):
    """
    Функция ищет в словаре cities города по ключу
    :param client_message_city: работа с str
    :return: строковое значение города или
    сообщение о победе
    """
    city_key_bot = (client_message_city[-1] if not
                client_message_city[-1] in ['ь', 'ы'] else
                client_message_city[-2])

    city_key_client = client_message_city[0].lower()
    cities[city_key_client].remove(client_message_city)

    if cities.get(city_key_bot) == None:
        return f'Вы выйграли! Я незнаю больше городов.'

    city_result = cities.get(city_key_bot)[0]
    cities[city_key_bot].remove(city_result)

    return city_result


print(game_city(city))
print(cities)