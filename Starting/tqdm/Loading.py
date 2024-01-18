from time import sleep

def loading(now, space, percent):
    str = f"{percent}%|"
    str += chr(0x2588) * int((now/7*7))
    str += chr(int(0x258F) - (now % 7)) if (now % 7) == 0 else ''
    str += (' ' * space)
    return str
    
def convert_percent(now, lnght):
    full = 78
    fill = int(now / lnght * full)
    space = full - fill
    percent = int(now / lnght * 100)
    return fill, space , percent
    
def ft_tqdm(numbers : range):
    for now in numbers:
        fill, space, percent = convert_percent(now, numbers[-1])
        print(loading(fill,space, percent)+ '|', end= '\r')
        yield
