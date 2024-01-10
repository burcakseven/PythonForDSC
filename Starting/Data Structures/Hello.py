
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

########
ft_list.pop(-1)
ft_list.append('World!')

ft_tuple = list(ft_tuple)
ft_tuple[1] = "Turkiye!"
ft_tuple = tuple(ft_tuple)

if ft_set.pop() == "Hello":
    ft_set.clear()
    ft_set.add("Hello")
ft_set = list(ft_set)
ft_set.append('İstanbul!')

ft_dict["Hello"] = '42Istanbul!'
########

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)