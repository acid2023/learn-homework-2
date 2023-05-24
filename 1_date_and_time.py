from datetime import datetime, timedelta, date
"""
Домашнее задание №2
 
Дата и время
 
1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime
 
"""


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = date.today()
    yesterday = today - timedelta(days=1)
    thirty_days_ago = today - timedelta(days=30)
    
    print(today)
    print(yesterday)
    print(thirty_days_ago)
 
def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    str2_datetime = datetime.now()
    str_date = str2_datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return  str_date
 
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))