def list_pattern(ipt_lst):
    if ipt_lst[0] == ipt_lst[1] or ipt_lst[1] != ipt_lst[2]:
        return False
    else:
        return True

ipt_lst = [x for x in input().split()]
result = list_pattern(ipt_lst)
print(result)
