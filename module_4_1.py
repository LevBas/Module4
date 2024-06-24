from fake_math import divide as fm
from true_math import divide as tm
first = int(input('Введите делимое: '))
second = int(input('Введите делитель: '))
print('В школьной математике ответ будет:', fm(first, second))
print('В высшей математике ответ будет:', tm(first, second))
