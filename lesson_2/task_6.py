"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
 Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет
 отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReportInfoName(ItemDiscount):
    def get_info(self):
        print(self.get_name)


class ItemDiscountReportInfoPrice(ItemDiscount):
    def get_info(self):
        print(self.get_price)


if __name__ == '__main__':
    product_1 = ItemDiscountReportInfoName('computer', 1000)
    product_2 = ItemDiscountReportInfoPrice('telephone', 500)

    product_1.get_info()
    product_2.get_info()

    def get_info(val):
        val.get_info()

    get_info(product_1)
    get_info(product_2)

    for i in (product_1, product_2):
        i.get_info()
