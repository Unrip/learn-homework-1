"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
QnAs = {"Как дела": "Хорошо!",
        "Что делаешь?": "Программирую",
        "Саня, ты в порядке?": "Да",
        "Главный вопрос жизни, вселенной и всего такого": "42"}


def ask_user_dict():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            question = input('Задай мне вопрос: ')
            if question in QnAs:
              print(QnAs[question])
            elif question.lower() == 'не хочу':
                print('Ну и ладно :(')
                break
            else:
                print("У меня нет ответа")
        except KeyboardInterrupt:
            print("Пока!")
            break


if __name__ == "__main__":
    ask_user_dict()
