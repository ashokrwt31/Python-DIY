import re

input_str = input("Enter an input string: ")
only_alphabets = re.match('^[a-zA-Z]+$',input_str)
numbers = re.match('^[0-9]+$',input)
alphanumeric = re.match('^[a-zA-Z0-9]+$',input_str)
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]').search(input_str)


if only_alphabets:
    print("Input string have only alphabets")
elif numbers:
    print("Input string have number")
elif alphanumeric:
    print("Input string is alpha-numeric")
elif special_char:
    print("Input string have special character")

else:
    print("This is not string")