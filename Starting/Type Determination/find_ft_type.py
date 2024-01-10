def all_thing_is_obj(object: any) -> int:
    
    type_str = str(type(object)).split("'")
    type_str = type_str[1]
    
    if type_str == "int":
        print("Type not found")
    elif type_str == "str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{type_str.capitalize()} : {type(object)}")
    
    return 42