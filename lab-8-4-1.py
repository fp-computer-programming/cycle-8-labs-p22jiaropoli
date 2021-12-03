# Author JRI 12/3/21

x = 0
while True:
    number = input("Please input a number ")
    if number == "-1":
        break
    else:
        x += int(number)
        
print("The sum of all the numbers entered is {}.".format(x))