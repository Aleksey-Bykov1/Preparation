"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def integer_equal_decimal(num: float) -> bool or None:
    """Проверка дробное ли число, если да - сравнение чисел до и после запятой
    :param num: float число
    :return: None - если целое число, True - числа до и после запятой равны,
    иначе False
    """
    int_dec = tuple(map(int, str(num).split('.')))
    if not int_dec[1]:
        print('Число целое')
    else:
        print('Число дробное')
        return int_dec[0] == int_dec[1]


if __name__ == '__main__':
    while True:
        try:
            number = float(input('Введите число: '))
        except ValueError:
            print(f'Необходимо ввести целое или дробно число!')
            continue
        print(integer_equal_decimal(number))
        break
