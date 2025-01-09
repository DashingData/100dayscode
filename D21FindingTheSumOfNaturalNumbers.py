# Python program to find the sum of the natural numbers 
num = int(input("Enter the Number:"))
if num < 0:
    print("Please Enter the Positive Number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1

    print(sum)

 