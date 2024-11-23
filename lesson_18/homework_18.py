import logging
from datetime import datetime


# Генератор
# 1. Напишите генератор, возвращающий последовательность четных чисел от 0 до N


def even_numbers_gen(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            yield i


print(list(even_numbers_gen(15)))
print('-'*80)


# Генератор
# 2. Создайте генератор, генерирующий последовательность Фибоначчи до определенного числа N


def fib_gen(max_num):
    first_num = 0
    second_num = 1
    while first_num < max_num:
        yield first_num
        first_num, second_num = second_num, first_num + second_num


print(list(fib_gen(100)))
print('-'*80)

# Итератор
# 1. Реализуй итератор для обратного вывода элементов списка


class ReverseListOutput:
    def __init__(self, numbers):
        self.nums = numbers
        self.current_id = len(self.nums)

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_id > 0:
            self.current_id -= 1
            return self.nums[self.current_id]
        raise StopIteration


list_of_numbers = [i for i in range(15+1)]
for el in ReverseListOutput(list_of_numbers):
    print(el, end=' ')
print()
print('-'*80)

# Итератор
# 2. Напишите итератор, возвращающий все четные числа в диапазоне от 0 до N


class EvenNumbersIterator:
    def __init__(self, max_number):
        self.current_num = 0
        self.max_num = max_number

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_num < self.max_num:
            self.current_num += 1
            if self.current_num % 2 == 0:
                return self.current_num
        raise StopIteration


for el in EvenNumbersIterator(7):
    print(el, end=' ')
print()
print('-'*80)


# Декораторы
# 1. Напишите декоратор, логирующий аргументы и результаты вызванной функции

logging.basicConfig(
    filename='login_system.log',
    level=logging.DEBUG,
    format=f'%(asctime)s -%(levelname)s -%(message)s')


def log(fn):
    def wrapper(*args, **kwargs):
        param = []
        if args:
            param.append(args)
        if kwargs:
            param.append(kwargs)
        if param:
            logging.debug(f'Параметры функции - \'{fn.__name__}\' - {param}')
        else:
            logging.debug(f'В функции - \'{fn.__name__}\' параметры отсуствуют')

        result = fn(*args, **kwargs)
        logging.debug(f'Результаты функции - \'{fn.__name__}\' - {result}')
        return result

    return wrapper


@log
def raising_to_power(number, degree):
    return number ** degree


raising_to_power(number=10, degree=3)


# Декораторы
# 2.Создайте декоратор, который перехватывает и обрабатывает исключения, возникающие при выполнении функции.


def decorator(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as er:
            print(f'Error in function \'{fn.__name__}\': {er}')
    return wrapper


@decorator
def div(a, b):
    print(a / b)


div(a=2, b=0)
