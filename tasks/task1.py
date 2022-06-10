# Default function to implement conditions to check leap year
def check_leap(year):
    # Checking if the given year is leap year
    if ((year % 400 == 0) or
            (year % 100 != 0) and
            (year % 4 == 0)):
        print("Given Year is a leap Year")
    # Else it is not a leap year
    else:
        print("Given Year is not a leap Year")


def type_year():
    # Taking an input year from user
    return input("Enter the Year: ")


def is_year_leap():
    # Printing result
    var = type_year()
    while var.isnumeric():
        check_leap(int(var))
        break
    else:
        print("incorrect input")
        is_year_leap()


is_year_leap()
