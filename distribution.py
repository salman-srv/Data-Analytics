def distributingMoney(x, y, z, K):
    total_money = x + y + z + K
    if total_money % 3 == 0:
        return 1
    else:
        return 0
   
x = int(input())
y = int(input())
z = int(input())
K = int(input())

result = distributingMoney(x, y, z, K)
print(result)
