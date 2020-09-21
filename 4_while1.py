"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        answer = input('Как дела? \nОтвет: ')
        if answer.lower() == 'хорошо':
            print('Вот и славно!')
            break
        else:
            print("Хочу, чтобы были хорошо)")

    
if __name__ == "__main__":
    ask_user()
