''' This is a program to remove the punctuations in our senstence'''

punctatutations  = """!@$#%^&*_+=-`~;':"\|.,/?"""
string = input("Enter anything here:")
empty_string = " "
for i in string:
    if i not in punctatutations:
        empty_string += i
print(empty_string)