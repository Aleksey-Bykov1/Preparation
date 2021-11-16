import os

"""
Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.

"""


def get_files(files: os.scandir) -> iter:
    """
    Функция возвращает yield-генератор путей и имён файлов в кортежах
    :param files: объект
    :return: yield-генератор из кортежей путей и имён файлов
    """

    for file in files:
        if file.is_dir():
            with os.scandir(os.path.abspath(file.path)) as files:
                yield from get_files(files)
        else:
            yield os.path.abspath(file.path), file.name


def print_directory_contents(sPath: str) -> None:
    """
    Функция распечатывает имена и пути файлов, в том числе вложенные
    :param sPath: путь до каталога
    """
    with os.scandir(sPath) as files:
        for file in get_files(files):
            print(file)


if __name__ == '__main__':
    print_directory_contents(os.getcwd())

#  Pull
