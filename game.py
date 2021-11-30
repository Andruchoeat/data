'''Игра угадай число'''

import numpy as np

number = np.random.randint(1, 101)  # загадываем число


# количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 1005'))
    
    if predict_number > number:
        print('Число должно быть меньше')
    elif predict_number < number:
        print('Число должно быть больше')
    else:
        print(f'Вы угадали это число = {number} за {count} попыток')
        break #конец игры и выход из цикла