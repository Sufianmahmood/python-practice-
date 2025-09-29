def multipy(*numbers):
    total=1
    for number in numbers:
        total *= number
    return total
print(multipy(2,4,5,45,55,3,2,3,4,55,67,7,8,8,8,6,5,4,2,4))