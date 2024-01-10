import sys

try:
    arg = sys.argv
    print(type(arg[1]))
    if len(arg) != 2 or not str.isdecimal(arg[1]):
        raise AssertionError("denem")
    
except AssertionError as a:
    print(a)
