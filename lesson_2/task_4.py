"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
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

    @get_price.setter
    def get_price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'name - {self.get_name}, price - {self.get_price}')


if __name__ == '__main__':
    product = ItemDiscount('computer', '1000')
    print(product.get_name, product.get_price)
    product_report = ItemDiscountReport(product.get_name, product.get_price)
    product_report.get_parent_data()

    product.get_price = '1100'
    print(product.get_name, product.get_price)
    product_report = ItemDiscountReport(product.get_name, product.get_price)
    product_report.get_parent_data()
