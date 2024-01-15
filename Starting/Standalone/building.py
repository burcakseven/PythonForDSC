'''def main():
# your tests and your error handling

  '''
import sys

def species_counter(arg : str):
    """
    Count the number of uppercase letters, lowercase letters, spaces, digits,
    and punctuation marks in the given text.

    Parameters:
    - arg (str): The input text.

    Returns:
    tuple: A tuple containing the count of characters, uppercase letters, lowercase letters,
           spaces, digits, and punctuation marks.
    """
    length = len(arg)

    upper = [char.isupper() for char in arg].count(True)
    lower = [char.islower() for char in arg].count(True)
    space = [char.isspace() for char in arg].count(True)
    digit = [char.isdigit() for char in arg].count(True)
    punctuation = length - ( upper + lower + space + digit)

    return length, upper, lower, space, digit, punctuation

def take_arg():
    """
    Get user input for the text to be analyzed.

    Returns:
    str: The user-provided text.

    Raises:
    AssertionError: If more than one command-line argument is provided.
    """
    arg = sys.argv

    try:
        if len(arg) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(arg) == 2:
            return arg[1]
        else:
            while((arg := input("What is the text to count?\n")) == ''):
                pass
            return arg

    except AssertionError as a:
        print(a)
        exit(1)

def main():
    
    length, upper, lower, space, digit, punctuation = species_counter(take_arg())
    print(f"The text contains {length} characters:")
    print(f"{upper} uppercase letters")
    print(f"{lower} lowercase letters")
    print(f"{space} spaces")
    print(f"{digit} digits")
    print(f"{punctuation} punctuation marks")

if __name__ == "__main__":
  main()