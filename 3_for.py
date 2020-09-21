"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main(classes_scores):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    students_num = 0
    school_scores_sum = 0

    for cls in classes_scores:
        scores_sum = sum(cls['scores'])
        school_scores_sum += sum(cls['scores'])
        students_num += len(cls['scores'])
        scores_class_avg = scores_sum / len(cls['scores'])
        print(f"Средняя оценка {cls['school_class']} класса - {scores_class_avg}")
    school_scores_avg = school_scores_sum / students_num
    print(f"Средняя оценка по школе - {school_scores_avg}")


if __name__ == "__main__":
    classes_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                      {'school_class': '5b', 'scores': [5, 5, 4, 5, 4, 3, 5]},
                      {'school_class': '7a', 'scores': [3, 5, 3, 5, 3, 5]},
                      {'school_class': '9v', 'scores': [2, 4, 3, 2]}]
    main(classes_scores)
