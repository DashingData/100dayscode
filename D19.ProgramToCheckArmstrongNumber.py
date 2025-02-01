# Program to check Armstrong Number
''' Armstrong number for example:
153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3)
          1 + 125 + 27 
          153
          as we can see same number aa gaya cube karne pe this is only armstromg number'''


num = int(input("Enter any three digit number:"))
sum = 0
temp  = num
''' yaha reminder ka logic lagao to seperate the numbers'''

''' then uss sperated number ka cube nikalo and ek variable bana do cube naam se'''
''' and that cube number mei sum kardo'''
''' now we have to remove that 3 as uska kaam poora ho gaya hai and now we have to
taken the other digit which is for example 5 so we will use floor i mean temop // 10
kar k use karegay'''
''' and follow the same pattern for other other number and the compare it with our num
if it is same then print that it is armstrong number'''

while temp > 0:
    digit = temp%10
    cube = digit ** 3
    sum = sum + cube
    temp //=  10
if sum == num:
    print("It is an armstrong number")
else:
    print("Not an armstong number") 


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

