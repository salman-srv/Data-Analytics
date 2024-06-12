def grade_calculator(n):
    if n >90:
        return "A"
    elif n >= 80 and n <= 89:
        return "B"
    elif n >= 70 and n <= 79:
        return "C"
    elif n >= 60 and n <= 69:
        return "D"
    elif n < 60:
        return "F"
percentage = int(input())
print(grade_calculator(percentage))
