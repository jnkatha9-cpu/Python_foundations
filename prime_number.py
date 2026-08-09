# Ask the user for a number
num = int(input("Enter a number: "))

# Start checking from 2
divisor = 2

# Assume the number is prime
is_prime = True

# Check divisibility of the number by all numbers from 2 to the number
while divisor < num:
    if num % divisor == 0:
        is_prime = False
        break

    divisor = divisor + 1

# Display the result
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
