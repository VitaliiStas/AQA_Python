# Write a function to create a list of all the even numbers in a list(using 'filter'&'lambda')
import random


def generate_random_list(min_range, max_range, num_count):
    # Generate "num_count" random numbers between "min_range" and "max_range"
    return random.sample(range(min_range, max_range), num_count)


def create_list_even_numbers(num_list):
    var = num_list
    even_list = list(filter(lambda x: (x % 2 == 0), num_list))
    print('The even list for the list ' + str(var) + ' is:')
    print(str(even_list))


create_list_even_numbers(generate_random_list(1, 1000, 10))
