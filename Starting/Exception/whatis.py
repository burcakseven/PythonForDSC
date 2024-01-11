import sys

def evenOddFunc(input):
    
    if(input % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")

try:
    arg = sys.argv
    if len(arg) != 2:
        if len(arg) > 1:
            raise AssertionError("more than one argument is provided")
        else:
            print("")
    elif not arg[1].isdigit():
        raise AssertionError("argument is not an integer")
    else:
        evenOddFunc(int(arg[1]))

except AssertionError as a:
    print("AssertionError: " + str(a))
    

