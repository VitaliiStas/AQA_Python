# check if number is prime or not
def type_number():
    return input('Type a number: ')


def type_and_check_number():
    'Function for the getting input from the user and checking if it int value'
    while True:
        var = type_number()
        if not var.isnumeric():
            print('Incorrect "value". Please type "int" value')
        else:
            break
    return int(var)


def check_if_num_prime(n):
    '''
    checking if num is prime
    num should be natural number greater than 1
    if input number is less than
    or equal to 1, it is not prime
    '''

    if n > 1:
        for i in range(2, n):
            if (n == 2):
                print(n, "is a prime number")
                break
            elif (n % i) == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")
    else:
        print(n, "is not a prime number")


check_if_num_prime(type_and_check_number())
