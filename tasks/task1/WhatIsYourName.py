'''
create a script which will ask "What's your name?" and then it will print "Hello, <name>"
'input()' -for reading from the console
'print()' - for the printing
'''


class WhatIsYourName:
    run_until = True

    while run_until:
        name = input("What is your name?: ")
        if name == "exit":
            run_until = False
        else:
            print("Hello, ", name)
            print("For exit type 'exit' ")
