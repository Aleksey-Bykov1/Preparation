"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться
результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский
классы (вторая и третья строка после объявления дочернего класса).
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


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        discount_price = self.get_price - self.get_price * (self.discount / 100)
        return f'discount price - {discount_price}'

    def get_parent_data(self):
        print(f'name - {self.get_name}, price - {self.get_price}')


if __name__ == '__main__':
    product = ItemDiscount('computer', 1000)
    print(product.get_name, product.get_price)
    product_report = ItemDiscountReport(product.get_name, product.get_price, 50)
    product_report.get_parent_data()

    print(product_report)
