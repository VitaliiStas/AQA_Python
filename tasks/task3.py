# multiply all the numbers in a list(using reduce and lambda)
from functools import reduce
import random


def generate_random_list(min_range,max_range,num_count):
    # Generate "num_count" random numbers between "min_range" and "max_range"
    def_list = random.sample(range(min_range, max_range), num_count)
    return def_list

def multiply_all_list(input_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    while True:
        lis = None
        var = str(input('Do you want use def list? (Y/N):').lower())
        if var == 'y':
            lis = input_list
            break
        elif var == 'n':
            lis = generate_random_list(1,100,10)
            break
        else:
            print('Please type correct answer')
    print('Result for the list: '+ str(lis))
    print(reduce(lambda x, y: x * y, lis))

multiply_all_list()