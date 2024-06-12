def list_multiply(num_list):
    r = 1
    for n in num_list:
        r *= n
    return r 

num_list = [int(x) for x in input().split()]
result=list_multiply(num_list )
print(result)
