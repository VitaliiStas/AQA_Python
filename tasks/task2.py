# Create a dictionary for 20th century
import pprint # pretty print for dict

start_year = 1901
end_year = 2001


# Default function to implement conditions to check leap year
def check_leap(year):
    # Checking if the given year is leap year
    if ((year % 400 == 0) or
            (year % 100 != 0) and
            (year % 4 == 0)):
        return 'leap year'
    else:
        return 'not leap year'


def print_dict_leap_no_leap():
    dict_1 = {year: check_leap(year) for year in range(start_year, end_year)}
    pprint.pprint(dict_1) # pretty print for dict

print_dict_leap_no_leap()