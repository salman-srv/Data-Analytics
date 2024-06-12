def Dict_change(name1, name2, name3):
    a = {"designation": 'Data scientist', "salary": 100000}
    f_data = {name1.strip().lower() : a.copy(), name2.strip().lower() : a.copy(), name3.strip().lower() : a.copy()}
    return f_data

name1 = str(input())
name2 = str(input())
name3 = str(input())
resulting_dict = Dict_change(name1, name2, name3)
print(resulting_dict)
