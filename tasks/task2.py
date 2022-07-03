# check if string is palindrome(the same from the reverse order)

def type_string():
    return str(input('Type a string: '))


def reverse_string(string):
    return string[::-1]


def check_if_palindrome(string):
    '''
    check if string is palindrome(the same from the reverse order)
    '==' is the same as '.__eq__'
    '''
    if string == reverse_string(string):
        print('String ' + "'" + string + "' is PALINDROME")
    else:
        print('String ' + "'" + string + "' NOT PALINDROME")

check_if_palindrome(type_string())

