def Dict_max_min(val1, val2, val3):
    my_dict = {'x': val1, 'y': val2, 'z': val3}
    a = max(my_dict.get('x'), my_dict.get('y'), my_dict.get('z'))
    b = min(my_dict.get('x'), my_dict.get('y'), my_dict.get('z'))
    return a , b 

val1 = int(input())
val2 = int(input())
val3 = int(input())
max_val, min_val = Dict_max_min(val1, val2, val3)
print("Maximum Value:", max_val)
print("Minimum Value:", min_val)
