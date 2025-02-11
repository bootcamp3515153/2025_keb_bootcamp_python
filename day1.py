
def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
                #is_prime = False
                #break
            #print(i, end=' ')
    else:
        return False
    return True
# main
#help(abs)
help(is_prime)

n = int(input("Input number: "))


if is_prime(n) :
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number")

