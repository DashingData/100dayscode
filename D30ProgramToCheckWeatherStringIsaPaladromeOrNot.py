# What is palidrom?
''' if we opposite any word and got the same word then this is known as palidrome'''

a = input("Enter a word here:")
rev = a[::-1]
if a == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
