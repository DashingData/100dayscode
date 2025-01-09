# program to swap two numbers

'''M-1 using third variable'''

x = int(input("Enter the value of x:"))
y = int(input("Enter the value for y: "))
temp = x 
x = y 
y = temp

print(f"The values of x is {x} and y is {y}" )



'''M-2 without using any third variable'''


x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))


x , y = y , x 

print(f"The value of x is {x} the value of y is {y}")