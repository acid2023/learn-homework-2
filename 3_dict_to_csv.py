"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import lorem
import random
import csv
 
def generate_dictionary_list():
    records_amount = random.randint(5, 20)
    dictionary_list = []
    dictionary_list.clear()
    for i in range(records_amount):
        name = lorem.sentence().split()[0].capitalize() + " " + lorem.sentence().split()[-2].capitalize()
        new_record = {'name': name, 'age': random.randint(18, 70), 'job': lorem.sentence()}
        dictionary_list.append(new_record)
    return dictionary_list
 
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dictionary_list = generate_dictionary_list()
    print(dictionary_list)
    with open('dictionaries.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for record in dictionary_list:
            writer.writerow(record)

if __name__ == "__main__":
    main()
