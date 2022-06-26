# Ask user to provide the information about employees
employees_list = []
employees_id_list = [1]
max_user_id = max(employees_id_list)


def type_info(info):
    while True:
        input_var = input(info)
        if not input_var.isnumeric():
            print('Incorrect "value". Please type "int" value for the user number')
        else:
            break
    return int(input_var)


def type_employee_info():
    return input("Please type employee info: ")


def add_employee_id():
    while True:
        print("do you know userid?(type y/n): ")
        run_until = input("type y/n: ")
        if run_until == "n":
            var = max(employees_id_list) + 1
            employees_id_list.append(var)
            return var
        elif run_until == "y":
            var = type_info("type user id: ")
            employees_id_list.append(var)
            return var
        else:
            print("you typed incorrect answer, please try again")


def type_employee_id():
    while True:
        var = add_employee_id()
        if employees_id_list.count(var) > 1:
            print("ID is present, please type correct id")
        else:
            return var


def provide_employees_information():
    user_num = type_info("How many users do you want to add?: ")
    for i in range(user_num):
        employees_list.append({str(type_employee_id()), type_employee_info()})
    print(str(employees_list))


provide_employees_information()
