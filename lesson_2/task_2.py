"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении
текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'name - {self.name}, price - {self.price}')


if __name__ == '__main__':
    product = ItemDiscount('computer', '1000')
    product_report = ItemDiscountReport(product.name, product.price)
    product_report.get_parent_data()
