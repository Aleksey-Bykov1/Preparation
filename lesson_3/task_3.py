"""
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться
значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""


def get_dict(keys: iter, values: iter) -> dict:
    """Создание словаря из ключей и значений,
    добавление None для ключей без значений
    :param keys: iter итерируемый объект с ключами
    :param values: iter итерируемый объект со значениями
    :return: dict словарь из входных итерируемых объектов
    """
    len_keys = len(keys)
    len_values = len(values)
    if len_values < len_keys:
        values_copy = values[:]
        for _ in range(len_keys - len_values):
            values_copy.append(None)
        new_dict = {key: value for key, value in zip(keys, values_copy)}
    else:
        new_dict = {key: value for key, value in zip(keys, values)}
    return new_dict


if __name__ == '__main__':
    keys_list = [1, 'abc', (1, 2), 5, 9, 0]
    values_list = ['lorem', 'ipsum', {'key': 'val'}]
    print(get_dict(keys_list, values_list))
