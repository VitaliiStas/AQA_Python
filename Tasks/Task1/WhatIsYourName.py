'''
create a script which will ask "What's your name?" and then it will print "Hello, <name>"
'input()' -for reading from the console
'print()' - for the printing
'''
run_untile = True
while run_untile:
    name = input("What is your name?: ")
    if name == "exit":
        run_untile = False
    else:
        print("Hello, ",name)
        print("For exit type 'exit' ")
