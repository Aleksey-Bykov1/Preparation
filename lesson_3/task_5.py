"""
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений заменить на значения
типа example345 (строка+число). Далее — усовершенствовать вторую функцию
из предыдущего примера (функцию извлечения данных). Дополнительно реализовать
поиск определенных подстрок в файле по следующим условиям: вывод первого
вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок
на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих
пробелы только в начале и конце — например, example345.
"""
import random
import re
import string
from os import getcwd
from os.path import join


def replacing_substring_file_output(path: str, substring) -> None:
    """Замена подстрок в файле. Вывод содержимого через регулярные выражения
    :param path: абсолютный путь файла
    :param substring: искомая подстрока
    """
    text = ''
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        pattern = f'{substring}\d*'
        new_value = '1234sfsdfsdf234235235'
        # вывод первого вхождения
        print(re.search(pattern, text))
        # вывод всех вхождений, далее идёт замена, по этому чтобы увидеть
        # вхождения паттерна выше, файл task_5.txt должен быть удалён!
        print(re.findall(pattern, text))
        # замена всех найденных подстрок на новое значение
        text = re.sub(pattern, new_value, text)

    with open(path, 'w+', encoding='utf-8') as file:
        file.write(text)

    lets_nums_spaces = '\s+\d+[a-zA-Z]+\w*\s+|\s+[a-zA-Z]+\d+\w*\s+'

    for el in re.findall(lets_nums_spaces, text):
        # вывод всех подстрок, состоящих из букв и цифр и имеющих
        # пробелы только в начале и конце — например, example345
        print(el)


def create_text_file(file_name: str, length=100) -> None:
    """Создавать текстовый файл из рандомных букв и цифр
    :param file_name: имя файла
    :param length: количество строк
    """
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            letters = string.ascii_lowercase
            rand_string = ''.join(
                random.choice(letters) for _ in range(length))
            texts_list = [letter * 23 for letter in rand_string]

            nums_list = [random.randint(0, 10000000000) for _ in range(length)]

            for idx in range(0, len(nums_list), 3):
                nums_list[idx] = f'example{nums_list[idx]}'
            texts_nums_zip = zip(texts_list, nums_list)

            for el in texts_nums_zip:
                file.write(f'{el[0]} {el[1]}\n')
    except FileExistsError:
        print('Файл уже существует!')
    finally:
        replacing_substring_file_output(
            join(getcwd(), file_name), substring='example')


if __name__ == '__main__':
    create_text_file('task_5.txt')
