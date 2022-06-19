# Print all values less than 5

num_list = []


def type_int(text):
    while True:
        input_var = input(text)
        if not input_var.isnumeric():
            print('Incorrect "value". Please type "int" value for the size')
        else:
            break
    return int(input_var)


def build_list():
    print("Create the list ")
    num = type_int("Please type list size: ")
    i = 1
    while i <= num:
        num_list.append(type_int("Type a number: "))
        i += 1


def print_all():
    build_list()
    print("All values les than 5: ")
    for el in num_list:
        if el < 5:
            print(el)


print_all()
