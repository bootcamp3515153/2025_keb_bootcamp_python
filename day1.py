# 세번째 과제

def my_pow(b,e) -> float:
    """
    Receive the base and exponent as input, and return the result of the exponentiation as a floating-point number.
    :param b: base number
    :param e: exponent number
    :return: float type
    """
    result = 1
    for k in range(e):
        result *= b
    return result


def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        #while i<(int(pow(num,0.5))+1) :
        while i*i < num+1:
            if num % i == 0:
                return False
            i += 1
    else:
        return False
    return True

first_num = int(input("Input first number: "))
second_num = int(input("Input second number: "))

if first_num > second_num :
    first_num, second_num = second_num, first_num

while first_num <= second_num :
    if is_prime(first_num) :
        print(f"{first_num} ")
    first_num += 1

