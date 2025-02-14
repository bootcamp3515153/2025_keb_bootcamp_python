def tg_abs(n) -> int:
    """
    Return absolute value of parameter n
    :param n:
    :return: absolute value
    """
    if n < 0:
        return -n
    return n


def tg_fibonacci_recursion(n) -> int:
    """
    Calculate fibonacci number (ver. recursive)
    :param n:
    :return: result value
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tg_fibonacci_recursion(n-2) + tg_fibonacci_recursion(n-1)


def tg_fibonacci_loop(n) -> int:
    """
    Calculate fibonacci number (ver. iterative)
    :param n:
    :return: result value
    """
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]

if __name__ != "__main__" :
    print("tgmath.py가 실행되었습니다.")