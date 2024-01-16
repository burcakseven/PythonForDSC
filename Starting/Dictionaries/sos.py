import sys

NESTED_MORSE = {' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def encode_morse(splitted):
    for word in splitted:
        for chr in word:
            print(NESTED_MORSE[str.upper(chr)], end='')
        print(' ',end='') #expanded space

def main():
    arg = sys.argv

    try:
        if len(arg) == 2:
            splitted = arg[1].split(' ')
            if ([word.isalnum() for word in splitted].count(False)) < 1:
                encode_morse(splitted)
            else:
                raise AssertionError("AssertionError: the arguments are bad")    
        else:
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as a:
        print(a)

if __name__ == "__main__":
    main()