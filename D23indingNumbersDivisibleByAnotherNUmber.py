# Using for Loop
num = int(input("Enter the Number:"))
print("The number divisible by 13 are:")
for i in range( 1 , 100):
    if i % num == 0:
        print(i)




# Using Anonymous Function/ Lambda Function and filter()

l = [23 , 24 , 25 , 30 , 75 , 98]
result = list(filter(lambda x : x % 5 == 0 , l))
print(result)

# Using the range function here and on applying the Anonymous fucntion
result = list(filter(lambda x : x % 5 == 0 , range(1 , 50)))
print(result)
