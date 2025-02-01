
# Program to display Multiplication Table

# By for "Loop"

def Multiplication_table(num):
    for i in range (1 , 11):
        result = num * i
        print(f"The table of {num} is : {num} * {i} = {result}")

num = int(input("Enter the number:"))
        
Multiplication_table(num)


# By using "While loop"


n = 7 
i = 1 
while i<=10:
    print(n , "x" , i , "="  , n*i)
    i += 1 
