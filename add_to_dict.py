def update_dictionary(original_dict, new_value):
    original_dict.update({1 : new_value})
    return original_dict

my_dict = {0: 10, 1: 20}
new_value = int(input())
n = update_dictionary(my_dict, new_value)
print(n)
