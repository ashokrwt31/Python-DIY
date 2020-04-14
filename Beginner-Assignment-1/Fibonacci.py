from functools import lru_cache

@lru_cache(maxsize= 1000)
def fibonacci(n):
    """Asks the user how many Fibonacci numbers to generate and generate them."""
    if type(n) != int:
        raise TypeError("n must be a integer.")
    if n < 1:
        raise TypeError("n must be a positive integer.")

    result = []
    if n == 1:
        result = [1]
    elif n == 2:
        result = [1,1]
    elif n > 2:
        result = [1, 1]
        i = 1
        while i < (n - 1):
            result.append(result[i] + result[i - 1])
            i += 1
    return result

print("Result fibonacci series is : ", fibonacci(int(input("Enter your value: "))))
