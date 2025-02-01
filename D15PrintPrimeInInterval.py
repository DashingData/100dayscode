# Program to print all the prime numbers in an interval
# Program to print all the prime numbers in an interval

# Taking the lower range of the interval as input from the user
lower = int(input("Enter the lower range: "))

# Taking the upper range of the interval as input from the user
upper = int(input("Enter the upper range: "))

# Loop through all numbers in the range [lower, upper] (inclusive)
for num in range(lower, upper + 1):
    # Prime numbers are greater than 1, so check only those numbers
    if num > 1:
        # Check if the number `num` has any divisors other than 1 and itself
        # Loop through possible divisors from 2 to the square root of `num`
        for i in range(2, int(num ** 0.5) + 1):  
            # If `num` is divisible by `i`, it is not a prime number
            if num % i == 0:
                break  # Exit the loop as we found a divisor
        else:
            # This `else` block executes only if the loop completes without a `break`
            # This means the number is prime
            print(num)  # Print the prime number



