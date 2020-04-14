import math

def check_input_number(message):
    """Check input number is positive integer or not."""
    while True:
       try:
          user_number = int(input(message))
          if user_number < 0:
              print("Not a positive integer! Try again.")
              continue
       except ValueError:
          print("Not an integer! Try again.")
          continue
       else:
          return user_number
          break

def sum_of_prime(number):
    """Sum of all n prime number logic."""
    sum1 = 0
    if number == 1:
       return 0
    if number == 2:
        return 2
    for num in range(2, number + 1):
        prime = True
        """Check for even number because these are not prime number."""
        if num > 2 and num % 2 == 0:
            continue
        """Check for only odd number and add if the number is not prime."""
        oddnumber = math.floor(math.sqrt(num))
        for d in range(3, 1 + oddnumber, 2):
            if num % d == 0:
                prime = False
                break
        if prime:
          sum1 = sum1 + num
    return sum1

number = check_input_number("Enter the positive number: ")
print("Sum of first %d prime numbers is: " % number,sum_of_prime(number))