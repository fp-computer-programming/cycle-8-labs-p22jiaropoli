# Author JRI 12/3/21

def sum_to(n):
    total = 0
    for x in range(n+1):
        total += x
    return total


number = input("Please input an integer ")

result = sum_to(int(number))
print(result)