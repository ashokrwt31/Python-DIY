
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

def reverse_number(num):
    """Reverse user enter positive integer."""
    reversenumber = 0
    while num > 0:
          temp = num % 10
          reversenumber = reversenumber * 10 + temp
          num = num // 10
    return reversenumber

number = check_input_number("Enter the positive number: ")
print("Reverse of the user enter positive number: ",reverse_number(number))
