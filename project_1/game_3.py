"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число


def random_predict_2(number: int = 1) -> int:
    """Рандомно угадываем число. Используем "бинарный поиск" каждый раз делим область возможных значений на 2

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
        int: Загаданное Число
    """
    # Задаем границы поиска
    start = 1 
    finish = 100
    count = 1
    # Реализация бинарного поиска 
    while True:
        n = (start + finish) // 2
        if number < n:
            finish = n - 1
        elif number > n:
            start = n + 1
        elif n == number:
            break
        count += 1
    return count, n

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_2(number)[0])

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict_2)






