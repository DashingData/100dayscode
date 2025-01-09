# To find the largest among three numbers 


x = int(input("Enter the first number:"))
y = int(input("Enter the second number"))
z = int(input("Enter the third number"))


if x > y and x > z:
    print(f"x is greater then y and z")
elif y > x and y > z:
    print("The y is greater then x and z") 
else:
    print("z is greater among all") 
