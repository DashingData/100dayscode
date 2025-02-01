# For finding the Factorial of a given number


#Using for loop 

num = int(input("Enter the number:"))
f = 1
if num < 0:
    print("Not a valid digit")
elif num == 0:
    print("The factorial is 1")
elif num > 0:
    for i in range(1 , num +1):
        f = f * i
print(f"The factorial of the number {num} is:" , f)





# Using recurssion (AGAR KOHI FUNCTION K ANDAR FUNCTION CALL KARTE Hai usko function bolte hai)
def factorial(a):
    if a == 0:
        return 1
    else:
        return ((a) * factorial(a-1))
num = int(input("Enter the number here:"))
result = factorial(num)
print("The factorial of the given number is" , result)