
def list_square(l1):
    l2 = []
    for i in l1:
        l2.append(i**2)
    return l2
       
num_list = [int(x) for x in input().split()]
print(list_square(num_list))
