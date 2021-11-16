"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться
фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию
подсчета процентов для пополняемой суммы. Причем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция — общую
сумму по вкладу на конец периода.
"""


def percent_deposit(summa: int, time_month: int) -> float:
    """
    Находим процент вклада
    :param summa: сумма вклада
    :param time_month: срок вклада в месяцах
    :return: процент вклада
    """
    bank_deposits = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )
    for dep in bank_deposits:
        if dep['begin_sum'] <= summa < dep['end_sum']:
            return dep[time_month]


def deposit(summa: int, time_month: int, charge: int) -> None:
    """
    Находим сумму вклада
    :param summa: сумма вклада
    :param time_month: срок вклада в месяцах
    :param charge: дополнительный ежемесячный вклад
    :return:
    """
    total = summa
    percent = percent_deposit(summa, time_month)
    for month in range(time_month):
        profit = total * percent / 100 / 12
        total += profit
        if month != 0 and month != time_month - 1:
            total += charge + charge * percent / 100 / 12

    print(f'{total:.2f}')


if __name__ == '__main__':
    deposit(4555, 12, 124)
