# 세번째 과제

def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num > 2:
        i = 2
        while i<=(int(pow(num,0.5))+1) :
            if num % i == 0:
                return False
            i += 1

    return True

first_num = int(input("Input first number: "))
second_num = int(input("Input second number: "))

while first_num <= second_num :
    if is_prime(first_num) :
        print(f"{first_num} ")
    first_num += 1

