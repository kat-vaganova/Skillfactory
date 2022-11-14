import numpy as np
from random import randint

set_number = np.random.randint(1, 100)
print(set_number)


def random_predict(number):
    """
    Рандомно угадываем число
    :param number: int Загаданное число
    :return: int число попыток
    """
    try_count = 0

    while True:
        guess_number = randint(1, 100)
        try_count += 1
        if set_number == guess_number:
            return try_count

    print(f'\n Guess number: {guess_number}. \n Try count: {try_count}')


random_predict(set_number)
