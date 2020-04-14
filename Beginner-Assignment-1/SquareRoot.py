
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

def square_of_list_element(userlist):
    """Calculate square of each element in user defined list."""
    result = []
    for ele in userlist:
        result.append(ele**2)
    return result

userlist = []
inputList = check_input_number("Enter number of elements in list: ")

for i in range(0, inputList):
    element = check_input_number("Enter positive number in %d position: " % (i + 1))
    userlist.append(element)

print("User enter list is :",userlist)
print("Square root of element in user enter list : ",square_of_list_element(usersqurelist))