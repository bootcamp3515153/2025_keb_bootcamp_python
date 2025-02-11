n = int(input("Input number: "))

is_prime = True
num = int(n**0.5)


if n>= 2:
    for i in range(2, num):
        if n % i == 0:
            is_prime = False
            break
else :
    is_prime = False

if is_prime == True :
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number")