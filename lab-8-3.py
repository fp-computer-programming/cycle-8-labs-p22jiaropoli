# Author JRI 12/2/21

def sum_to(n):
    total = 0
    x = 0
    while x <= int(n):
        total += x
        x += 1
    return total


number = input("enter an integer ")
print(sum_to(number))
