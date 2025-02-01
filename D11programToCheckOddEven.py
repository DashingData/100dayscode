# To cheeck if the given number is odd or even

x = int(input("Enter the number:"))
if x % 2 == 0:
    print("The number is even")
elif x % 2 != 0:
    print("The number is odd")
else:
    print("Invalid input")