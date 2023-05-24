"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    str_length = len(content)
    words_count = len(content.split())
    print(str_length)
    print(words_count)
    content = content.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as f:
           f.write(content)
           
if __name__ == "__main__":
    main()
