#First Assignment
# 2중 데코레이터 적용, 성능측정(시간측정) 데코레이터, 디스크림션 데코레이터를 팩토리얼 함수에 적용하시오.

import time

def discri_decorator(func):
    def wrapper(*arg):
        print(f'함수 이름 : {func.__name__}')
        print(f'함수 설명 : {func.__doc__}')
        r = func(*arg)
        return r
    return wrapper

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e-s}초')
        return r
    return wrapper

@time_decorator
@discri_decorator
def factorial_repetition(n) -> int:
    """
    Function to calculate factorial using a loop
    :param n: Number to calculate factorial
    :return: result
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input('Please enter a number to calculate its factorial.\n>>'))
print(f"결과 : {number}! = {factorial_repetition(number)}")