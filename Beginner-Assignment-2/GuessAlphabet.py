# Write a program which asks the user to guess a predefined alphabet. Raise custom
# exceptions if the entered alphabet entered if smaller or greater than the predefined
# alphabet.

class Error(Exception):
    """Parent class for other exceptions"""
    pass

class AlphabetIsSmallError(Error):
    """Raised exception when the input alphabet is small"""
    pass

class AlphabetIsLargeError(Error):
    """Raised exception when the input alphabet is large"""
    pass


def check_other_alphabet(alpha1, alpha2):
    """Check entered alphabet is guessed correctly or not with custom exception"""
    try:
        if ord(alpha1) > ord(alpha2):
           raise AlphabetIsSmallError
        elif ord(alpha1) < ord(alpha2):
            raise AlphabetIsLargeError
        else:
            print("Congratulations!, You guessed correct alphabet.")
            return True
    except AlphabetIsSmallError:
           print("This alphabet is small from predefine alphabet, try again!")
           pass
    except AlphabetIsLargeError:
            print("This alphabet is large from predefine alphabet, try again!")
            pass
    else:
            pass

predefine_alpha = "h"

while True:
    """Enter a valid alphabet for guessing with predefined alphabet"""
    char2 = (input("\nPlease enter valid alphabet  "))
    if not char2.isalpha():
        print("Enter valid alphabet, This is not alphabet.")
        continue
    elif len(char2) > 1:
        print("Enter valid alphabet.")
        continue
    elif (65 <= ord(char2) <= 90) or (97 <= ord(char2) <= 122):
        isSuccess = check_other_alphabet(predefine_alpha, char2)
        if isSuccess:
            break


