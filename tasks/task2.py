# Email checking

sufix_for_check = "@eleks.com"
email_for_check = "tes#tEmail@eleks.com"
list = ["#", "!", "%", "*"]


def type_email():
    # Taking an input year from user
    return input("Enter the email: ")


def email_char_check(string):
    for el in list:
        if string.count(el) > 0:
            print("Email format incorrect.Inappropriate char is present: " + "'" + el + "'")
            break


def email_validator(email):
    email_char_check(email)
    if email_for_check.count("@") > 1:
        print("Email format incorrect.Extra '@' is present ")
    elif not email.endswith(sufix_for_check):
        print("Email format incorrect.Incorrect domain ")
    else:
        print("Email is correct")


email_validator(email_for_check)
