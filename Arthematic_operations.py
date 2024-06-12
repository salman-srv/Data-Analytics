def perform_arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulus = a % b
    
    return [addition, subtraction, multiplication, division, modulus]
    # Write your function here
   
a = int(input())
b = int(input())
print(perform_arithmetic_operations(a, b))
