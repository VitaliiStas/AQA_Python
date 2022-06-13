# Print all values less than 5

num_list = []


def type_int(text):
    return input(text)


def build_list():
    print("Create the list ")
    num = int(type_int("Please type list size: "))
    i = 1
    while i <= num:
        num_list.append(int(type_int("Type a number: ")))
        i += 1


def print_all():
    build_list()
    print("All values les than 5: ")
    for el in num_list:
        if el < 5:
            print(el)

print_all()