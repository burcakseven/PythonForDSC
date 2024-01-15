print(filter.__doc__)

def ft_filter(func, iterable):
    '''
    filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    '''
    try:
        if func is None:
            return [item for item in iterable if bool(item)]
        return [item for item in iterable if func(item)]

    except Exception as e:
        print("Error.")
    return None
