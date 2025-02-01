# Anonymus Functions is also know as lambda Function 

nterms = int(input("Enter the number of terms:"))
result = list(map(lambda x : 2 ** x , range(nterms+1)))
print(result)





# Using for Loop


nterms = int(input("Enter the number of terms:"))
result = list(map(lambda x : 2 ** x , range(nterms+1)))
print(result)


for i in range (nterms + 1):
    print("The values of 2 raised to power" , i , "is" , result[i])
