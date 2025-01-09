# Program to Find out the armstong number in the particular given series 

# Suppose if the number of digits is greater then 3 
num = int(input("Enter the number:"))
order = len(str(num))
sum = 0 
temp = num
while temp > 0:
    digit = temp % 10
    cube = digit ** order
    sum = sum + cube
    temp //= 10
if sum == num:
    print("The number is an armstong Number:")
else:
    print("The number is not a armstong number:")