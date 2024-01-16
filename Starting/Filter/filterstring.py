from ft_filter import ft_filter
import sys

def filter_string(splitted, min_limit : int):
    f = lambda x: x if(x>min_limit) else None
    lenghts_of_elements = [words for words in splitted if f(len(words)) != None]
    return lenghts_of_elements
    
def main():
    
    arg = sys.argv                                           
    try:
        if len(arg) == 3:
            splitted = arg[1].split(' ')
            if not sum([not word.isalnum() for word in splitted]) and arg[2].isdecimal():
                print(filter_string(splitted, int(arg[2])))
            else:
                raise AssertionError("AssertionError: the arguments are bad")
        else:
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as a:
        print(a)
        exit(1)
        
if __name__ == "__main__":
  main()