# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        self.i += 1
        if self.i >= self.n:
            raise StopIteration()
        for number in range(self.i, self.n + 1):
            for prime in range(2, self.i + 1):
                if number > prime and number % prime == 0:
                    self.i += 1
                    if self.i >= self.n:
                        raise StopIteration()
                    break
            else:
                return number




# prime_number_iterator = PrimeNumbers(n=1000)
# started_at = time.time()
# for number in prime_number_iterator:
#     print(number)
# ended_at = time.time()
# elapsed = round(ended_at - started_at, 4)
# print(f'Функция работала {elapsed} секунд(ы)')




    # TODO здесь ваш код





# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик



def prime_numbers_generator(n):
    for number in range(2, n + 1):
        for prime in range(2, number):
            if number % prime == 0:
                break
        else:
            yield number






# started_at = time.time()
# for number in prime_numbers_generator(n=10000):
#     print(number)
# ended_at = time.time()
# elapsed = round(ended_at - started_at, 4)
# print(f'Функция работала {elapsed} секунд(ы)')


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def happy_dig(dig):
    str_dig = str(dig)
    first_half = 0
    second_half = 0
    half_len = int(len(str_dig)/2)
    for i in range(0, half_len):
        first_half += int(str_dig[i])
        second_half += int(str_dig[::-1][i])
    return first_half == second_half







def prime_numbers_generator(n,n1):
    for number in range(2, n + 1):
        for prime in range(2, number):
            if number % prime == 0:
                break
        else:
            if n1 == 1 and happy_dig(number):
                yield number
            elif n1 == 2 and palindrome(number):
                yield number

def happy_dig(dig):
    str_dig = str(dig)
    first_half = 0
    second_half = 0
    half_len = int(len(str_dig)/2)
    for i in range(0, half_len):
        first_half += int(str_dig[i])
        second_half += int(str_dig[::-1][i])
    return first_half == second_half




def palindrome(dig):
    str_dig = str(dig)
    return str_dig == str_dig[::-1]


started_at = time.time()
for number in prime_numbers_generator(n=100000, n1=2):
    print(number)
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Функция работала {elapsed} секунд(ы)')