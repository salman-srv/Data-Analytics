arr = [int(x) for x in input().split()]
count=0
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if arr[i]==arr[j]:            
      count+=1
      break
print(count)
