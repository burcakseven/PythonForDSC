from ft_filter import ft_filter
import sys

def filter_string(arg):
    pass
    
def main():
    
    arg = sys.argv()
    try:
        if len(arg) == 3:
            if arg[1].isprintable() and arg[1].isdecimal():
                filter_string(arg)
        else:
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as a:
        print(a)
        exit(1)
        
if __name__ == "__main__":
  main()