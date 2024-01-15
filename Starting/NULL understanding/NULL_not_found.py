def NULL_not_found(object: any) -> int:

    NULL_dict = {None: "Nothing", 0 : "Zero", '' : "Empty", False : "Fake"}
    if object != object:
        print("Cheese: nan <class 'float'>")
    elif object in NULL_dict:
        print(f"{NULL_dict[object]}: {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0