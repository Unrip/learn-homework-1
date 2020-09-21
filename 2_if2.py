"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main(first_string, second_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    answer = 0
    if isinstance(first_string, str) and isinstance(second_string, str):
        if first_string == second_string:
            answer = 1
        elif second_string == 'learn':
            answer = 3
        elif len(first_string) > len(second_string):
            answer = 2
        else:
            answer = 'нет такого варианта'
    return answer


if __name__ == "__main__":
    examples = [
        ('строка', 123),
        ('просто строка', 'просто строка'),
        ('long first string', 'second string'),
        ('string', 'learn'),
        ('string', 'long string')
    ]
    for n, m in examples:
        print(main(n, m))
