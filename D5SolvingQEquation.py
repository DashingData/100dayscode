# python program to solve Quadrtatic equation 
# quadratic equation ax**2 + bx + c = 0 
# a , b and c are real numbers 
# a!= 0 
import cmath

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the thord number:"))

# formula for discriminant

d = (b**2)-(4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("The root of the equation is" , root1 ,"and" , root2) 
