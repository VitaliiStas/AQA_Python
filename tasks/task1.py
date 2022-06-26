# Print a tuple of leap years of the 20th century

start_year = 1901
end_year = 2001


# Default function to implement conditions to check leap year
def check_leap(year):
    # Checking if the given year is leap year
    if ((year % 400 == 0) or
            (year % 100 != 0) and
            (year % 4 == 0)):
        return True
    else:
        return False


# def gen_leap_year_list():
#     years_lisr = []
#     for x in range(start_year, end_year):
#         if check_leap(x):
#             years_lisr.append(x)
#         else:
#             continue
#     return years_lisr


# tuple_1 = tuple(gen_leap_year_list())

tuple_1 = tuple(x for x in range(start_year, end_year) if check_leap(x) is True)

print(tuple_1)
