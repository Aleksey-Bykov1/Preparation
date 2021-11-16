import random

"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по
шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""


def random_num(start: int, end: int, quantity: int) -> None:
    """
    Генерирует список случайных чисел и заполняет их в список и словарь
    :param start: начальное число генерации
    :param end: конечное число генерации
    :param quantity: количество генераций случайного числа
    """
    list_num = []
    for _ in range(quantity):
        rand_num = random.randint(start, end)
        if rand_num != 0:
            list_num.append(rand_num)
    print(list_num)

    dict_num = {}
    for i in range(quantity):
        rand_num = random.randint(start, end)
        if rand_num != 0:
            dict_num.update({f'elem_{i}': rand_num})
    print(dict_num)


if __name__ == '__main__':
    random_num(-3, 12, 7)
