# Program to check if the number is positive negative or zero


x = int(input("Enter the number:"))


if x < 0:
    print(f"The number {x} is negative")
elif x > 0:
    print(f"The number {x} is postive")
elif x == 0:
    print(f"The number is zero")
else:
    print("Invalid input") 
               
