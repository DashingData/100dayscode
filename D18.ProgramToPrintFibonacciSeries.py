# Python program to print the fibonacci series
a = 0  # Fabonnaci series mei every time first element zero hota hai 
b = 1  # and second element evey time 1 hota hai  
c = a + b  #and the third number will be the sum of last two numbers 
num = int(input("Enter the number to print fabonnaci series:")) # taking the num till where we have to print fabbonaci series
if num == 1:  # yaha specify kiya hai gaya hai ki if num = 1 hai tho seedha he print kardo 

    print(a)
else:
    print(a)    # agar num = 1 nhi hai and one se bada he hai then in this case we have to print bothe "a" and "b" because they are mandatory 
    print(b)
    for i in range (1 , num + 1):  # and for the thied number we have to use a loop because in this we have to print the sum of the last two numbers 
        c = a+b   # lopp mei simply ye hai ki 1 se num + 1 thak jayega loop and their jub vo print ho jayega then a = b ho jayega and b = c ho jayega  
        a = b 
        b = c 
        print(c)


''' yaha one think is to be noted that "a" and "b" yaha already print
hogay he so in that case agar hum yaha 10 daalgay num mei tho yaha pe 
12 numebers print hokar ayegay because yaha pe already 2 numers specified hai 
i mean "a" and "b" '''