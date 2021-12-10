"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой
информацией. Для создания списков использовать генераторы.
Применить к спискам функцию zip(). Результат выполнения этой функции
должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный
вывод содержимого. Вся программа должна запускаться по вызову первой функции.
"""
import random
import string
from os import getcwd
from os.path import join


def file_output(path: str) -> None:
    """Построчный вывод содержимого файла
    :param path: абсолютный путь файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line)


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

            texts_nums_zip = zip(texts_list, nums_list)

            for el in texts_nums_zip:
                file.write(f'{el[0]} {el[1]}\n')
    except FileExistsError:
        print('Файл уже существует!')
    finally:
        file_output(join(getcwd(), file_name))


if __name__ == '__main__':
    create_text_file('task_4.txt')
